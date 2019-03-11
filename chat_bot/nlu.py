#!/usr/bin/env python

import os
import sys
import subprocess


class NLU(object):
    def __init__(self, **kwargs):
        self.kwargs = {k: v for k, v in kwargs.items()}
        self.cwd = os.getcwd()

    def train_nlu_docker(self):
        """execute docker run command to either the spacy or tensorflow pipeline to train rasa_nlu
         using word embedding or RNN
        """
        print('Training spacy model to classify intents and extract identities', file=sys.stderr)
        try:
            cmd = ['docker', 'run', '--rm',
                   '-v', self.cwd + ':/app/project',
                   '-v', self.cwd + '/models/rasa_nlu:/app/models',
                   '-v', self.cwd + '/config:/app/config',
                   'rasa/rasa_nlu:latest-tensorflow',
                   'run', 'python', '-m', 'rasa_nlu.train', '-c', 'config/nlu_config.yml', '-d', 'project/data/nlu_data.md',
                   '-o', 'models',
                   '--project', 'chatbot'
                   ]
            p = subprocess.call(cmd)
            if p == 0:
                print('nlu training complete', file=sys.stderr)

        except Exception as e:
            print(e)

    def start_nlu_server(self):
        """start the nlu stand alone server to test intent classifier
        test -> curl -XPOST localhost:5000/parse -d '{"q":"hello there", "project": "chatbot"}'

        Returns: blocking twisted web server instance that accepts rest queries at localhost:5000

        """
        try:
            dir = self.cwd + '/models/rasa_nlu/chatbot'
            cmd = ['docker', 'run', '--rm', '-p', '5000:5000',
                   '-v', dir + ':/app/projects/chatbot', 'rasa/rasa_nlu:latest-tensorflow',
                   'start', '--path', '/app/projects', '--port', '5000'
                   ]
            p = subprocess.call(cmd)

        except Exception as e:
            print(e)