#!/usr/bin/env python
import rasa_core.policies
from rasa_nlu.training_data import load_data
from rasa_nlu.model import Trainer
from rasa_nlu import config as nlu_config
from rasa_core.train import train_dialogue_model
from rasa_nlu.model import Interpreter
from rasa_core.interpreter import NaturalLanguageInterpreter
from rasa_core.agent import Agent
from rasa_core.training import interactive  # renamed from online
from rasa_core.policies.keras_policy import KerasPolicy
from rasa_core.policies.memoization import MemoizationPolicy
from rasa_core.policies.sklearn_policy import SklearnPolicy
from rasa_core import utils
import pprint
import sys
import argparse
import os
import traceback


# TODO: add logging
# TODO: add form action for medicine
# TODO: add custom action to search side effects

class Train(object):
    def __init__(self, **kwargs):
        self.kwargs = {k: v for k, v in kwargs.items()}
        self.do_train_nlu = self.kwargs.get('do_train_nlu', False)
        self.do_train_core = self.kwargs.get('do_train_core', False)
        self.nlu_data = self.kwargs.get('nlu_data', 'data/nlu.md')
        self.domain_file = self.kwargs.get('domain_file', 'domain.yml')
        self.nlu_model_dir = self.kwargs.get('nlu_model_dir', 'models')
        self.core_config_file = self.kwargs.get('core_config_file', 'config/core_config.yml')
        self.nlu_config_file = self.kwargs.get('nlu_config_file', 'config/nlu_config.yml')
        self.stories_file = self.kwargs.get('stories_file', 'data/stories.md')
        self.core_model_dir = self.kwargs.get('core_model_dir', 'models/dialogue')
        self.endpoints_config_file = self.kwargs.get('endpoints_config_file', 'config/endpoints.yml')
        self.cwd = os.getcwd()
        utils.configure_colored_logging(loglevel='DEBUG')

    def train_nlu(self):
        """Trains the underlying pipeline using the provided training data"""
        training_data = load_data(self.nlu_data)
        trainer = Trainer(nlu_config.load(self.nlu_config_file))
        trainer.train(training_data)
        trainer.persist(self.nlu_model_dir, fixed_model_name="nlu")

    def predict_intent(self, text):
        """loads the trained model, parses the text argument and returns the predicted intent
        from the rasa nlu intent classifier

        Returns: json result with predicted intent score for all intents

        """
        interpreter = Interpreter.load('models/default/nlu')
        pprint.pprint(interpreter.parse(text))

    def train_core(self):
        """train rasa core model

        Returns:

        """
        print('training core model', file=sys.stderr)
        agent = Agent('domain.yml', policies=[MemoizationPolicy(), KerasPolicy(), SklearnPolicy(), rasa_core.policies.FormPolicy()])  # training pipeline to use (i.e. RNN, embeddings)
        training_data = agent.load_data(self.stories_file)

        #  passing policy settings to the train function is not supported anymore
        #  put in the policy config (config/core_config.yml) instead
        trainer = train_dialogue_model('domain.yml', self.stories_file, self.core_model_dir, policy_config=self.core_config_file)
        trainer.persist(self.core_model_dir)

    def train_interactive(self):
        """create nlu and core agents from trained models and start interactive training
        * model policies are specified in config/core_config.yml
        * KerasPolicy by default uses LSTM

        """
        _interpreter = NaturalLanguageInterpreter.create('models/default/nlu')
        #  train_dialogue_model returns agent object
        train_agent = train_dialogue_model(domain_file=self.domain_file,
                                           stories_file=self.stories_file,
                                           output_path=self.core_model_dir,
                                           policy_config=self.core_config_file,
                                           interpreter=_interpreter
                                           )
        interactive.run_interactive_learning(train_agent, skip_visualization=True)
        train_agent.persist(self.core_model_dir)

    @classmethod
    def parse_arg(cls):
        parser = argparse.ArgumentParser(usage=None, description='train rasa nlu and core models')
        parser.add_argument('--nlu', dest='nlu', action='store_true', help='train the natural language model')
        parser.add_argument('--predict_intent', dest='string', help='get nlu prediction for string')
        parser.add_argument('--core', dest='core', action='store_true', help='train the core neural network')
        parser.add_argument('--both', dest='both', action='store_true', help='train nlu and core')
        parser.add_argument('--interactive', dest='interactive', action='store_true', help='train nlu and core interactively')

        args = parser.parse_args()
        if len(sys.argv) == 1:
            parser.print_help()
            sys.exit()

        train_obj = Train()

        try:
            if args.nlu:
                print('nlu')
                cls.train_nlu(train_obj)
            elif args.core:
                print('core')
                cls.train_core(train_obj)
            elif args.both:
                print('both')
                cls.train_nlu(train_obj)
                cls.train_core(train_obj)
            elif args.string:
                cls.predict_intent(train_obj, args.string)
            else:
                print('interactive')
                cls.train_interactive(train_obj)
        except Exception as e:
            traceback.print_exc()


def main():
    t = Train.parse_arg()
    # t = Train().train_interactive()


if __name__ == "__main__":
    main()
