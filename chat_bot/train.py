#!/usr/bin/env python

import os

from rasa_nlu.training_data import load_data
from rasa_nlu.model import Trainer
from rasa_nlu import config
from rasa_core import config
from rasa_nlu.model import Interpreter
from rasa_core.interpreter import NaturalLanguageInterpreter
from rasa_core.agent import Agent
from rasa_core import train
from rasa_core.training import interactive  # renamed from online
from rasa_core.policies.keras_policy import KerasPolicy
from rasa_core.policies.memoization import MemoizationPolicy
from rasa_core.policies.sklearn_policy import SklearnPolicy
from rasa_core import utils
import pprint
import shutil
import subprocess
import sys


class Train(object):
    def __init__(self, **kwargs):
        self.kwargs = {k: v for k, v in kwargs.items()}
        self.do_train_nlu = self.kwargs.get('do_train_nlu', False)
        self.do_train_core = self.kwargs.get('do_train_core', False)
        self.cwd = os.getcwd()
        utils.configure_colored_logging(loglevel='DEBUG')

        # if self.do_train_nlu:
        #     self.train_nlu_docker()
        # elif self.do_train_core:
        #     self.train_core()
        # elif self.do_train_nlu and self.do_train_core:
        #     pass
        # else:
        #     self.nlu_model_dir = 'models/default/chat_bot'



    def predict_intent(self, text):
        """loads the trained model, parses the text argument and returns the predicted intent
        from the rasa nlu intent classifier

        Returns: json result with predicted intent score for all intents

        """
        interpreter = Interpreter.load('models/rasa_nlu/chatbot/chatbot')
        pprint.pprint(interpreter.parse(text))

    def train_core(self):
        """train a rasa core model

        Returns:

        """
        config_file = 'config/core_config.yml'
        config.load(config_file)
        training_data_file = 'data/stories.md'  # data to train model with
        trained_model_path = 'models/dialogue'  # location of trained model
        agent = Agent('domain.yml', policies=[MemoizationPolicy(), KerasPolicy(), SklearnPolicy()])  # training pipeline to use (i.e. RNN, embeddings)
        training_data = agent.load_data(training_data_file)

        #  passing policy settings to the train function is not supported anymore
        #  put in the policy config instead
        agent.train(training_data)  # TODO: load core_config.yml
        agent.persist(trained_model_path)

    def train_interactive(self):
        _interpreter = NaturalLanguageInterpreter.create('models/rasa_nlu/current/chatbot')
        train_agent = train.train_dialogue_model(domain_file='domain.yml',
                                   stories_file='data/nlu_data.md',
                                   output_path='models/dialog',
                                   policy_config='config/core_config.yml',
                                   endpoints='config/endpoints.yml',
                                   interpreter=_interpreter)
        interactive.run_interactive_learning(train_agent)



