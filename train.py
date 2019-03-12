#!/usr/bin/env python

import os

import examples.concertbot.train_interactive
from rasa_nlu.training_data import load_data
from rasa_nlu.model import Trainer
from rasa_nlu import config as nlu_config
from rasa_core import config as core_config
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

        if self.do_train_nlu and self.do_train_core:
            self.train_nlu()
            self.train_core()
        elif self.do_train_core and not self.do_train_nlu:
            self.train_core()
        elif self.do_train_nlu and not self.do_train_core:
            self.train_nlu()
        else:
            do_interactive = input('Do you want to train interactively? (yes/no) ')
            if do_interactive in ['yes', 'Yes', 'y', 'Y', 'YES']:
                self.train_interactive()
            print('Please set do_train_nlu | do_train_core boolean value', file=sys.stderr)

    def train_nlu(self):
        """Trains the underlying pipeline using the provided training data"""
        training_data = load_data(self.nlu_data)
        trainer = Trainer(nlu_config.load(self.nlu_config_file))
        trainer.train(training_data)
        self.nlu_model_dir = trainer.persist(self.nlu_model_dir, fixed_model_name='chat_bot')

    def predict_intent(self, text):
        """loads the trained model, parses the text argument and returns the predicted intent
        from the rasa nlu intent classifier

        Returns: json result with predicted intent score for all intents

        """
        interpreter = Interpreter.load(self.nlu_model_dir)
        pprint.pprint(interpreter.parse(text))

    def train_core(self):
        """train a rasa core model

        Returns:

        """
        print('training core model', file=sys.stderr)
        # config_file = 'config/core_config.yml'
        # stories_file = 'data/stories.md'  # data to train model with
        # trained_model_path = 'models/dialogue'  # location of trained model
        agent = Agent('domain.yml', policies=[MemoizationPolicy(), KerasPolicy(), SklearnPolicy()])  # training pipeline to use (i.e. RNN, embeddings)
        training_data = agent.load_data(self.stories_file)

        #  passing policy settings to the train function is not supported anymore
        #  put in the policy config instead
        trainer = train_dialogue_model('domain.yml', self.stories_file, self.core_model_dir, policy_config=self.core_config_file)
        # agent.train(training_data)
        # agent.persist(trained_model_path)
        trainer.persist(self.core_model_dir)

    def train_interactive(self):
        agent = Agent('domain.yml', policies=[MemoizationPolicy(), KerasPolicy(), SklearnPolicy()])  # training pipeline to use (i.e. RNN, embeddings)
        # training_data = agent.load_data(self.stories_file)
        _interpreter = NaturalLanguageInterpreter.create('models/default/chat_bot')
        train_agent = train_dialogue_model(domain_file=self.domain_file,
                                           stories_file=self.stories_file,
                                           output_path=self.core_model_dir,
                                           policy_config=self.core_config_file,
                                           interpreter=_interpreter
                                           )
        interactive.run_interactive_learning(train_agent, skip_visualization=True)
        train_agent.persist(self.core_model_dir)


