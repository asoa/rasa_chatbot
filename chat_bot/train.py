#!/usr/bin/env python

import os
import subprocess
import shutil
import sys
from rasa_nlu import config
from rasa_nlu.training_data import load_data
from rasa_nlu.model import Trainer
from rasa_nlu import config
from rasa_nlu.model import Interpreter


class Train(object):
    def __init__(self, **kwargs):
        self.kwargs = {k: v for k, v in kwargs.items()}
        self.do_train = self.kwargs.get('do_train', False)
        self.cwd = os.getcwd()
        if self.do_train:
            self.train_nlu()
            # self.train_nlu_manual('chat_bot/data', 'chat_bot/config/nlu_config.yml', 'chat_bot/models/rasa_nlu')

    def train_nlu(self):
        """execute docker run command to either the spacy or tensorflow pipeline to train rasa_nlu
         using word embedding or RNN
        """
        print('Training spacy model to classify intents and extract identities', file=sys.stderr)
        try:
            shutil.rmtree(os.path.join(self.cwd, 'models'))
            cwd = os.getcwd()
            cmd = ['docker', 'run', '--rm',
                   '-v', cwd + ':/app/project',
                   '-v', cwd + '/models/rasa_nlu:/app/models',
                   '-v', cwd + '/config:/app/config',
                   'rasa/rasa_nlu:latest-spacy',
                   'run', 'python', '-m', 'rasa_nlu.train', '-c', 'config/nlu_config.yml', '-d', 'project/data/',
                   '-o', 'models',
                   '--project', 'current',
                   '--fixed_model_name', 'chatbot'
                   ]

            p = subprocess.check_output(cmd)
        except Exception as e:
            print(e)

    def train_nlu_manual(self, data_md, config_file, model_dir):
        training_data = load_data(data_md)
        trainer = Trainer(config.load(config_file))
        trainer.train(training_data)
        model_output = trainer.persist(model_dir, fixed_model_name='chat_bot')


    def predict_intent(self, text):
        """loads the trained model, parses the text argument and returns the predicted intent
        from the rasa nlu intent classifier

            ** need to install: python -m spacy download en

        Returns: json result with predicted intent score for all intents

        """
        path = '/Users/asoa/PycharmProjects/664/rasa_chat_bot/chat_bot/models/rasa_nlu/current/chatbot'
        interpreter = Interpreter.load(path)
        print(interpreter.parse(text))

    def train_nlu_tensorflow(self):
        pass

    def train_core(self):
        pass


def main():
    pass


if __name__ == "__main__":
    main()
