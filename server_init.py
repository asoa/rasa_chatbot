#!/usr/bin/env python
import argparse
import threading
import subprocess
import multiprocessing
from io import StringIO


class Server(object):
    """utility script to start/kill action server or nlu server
    """
    def __init__(self, **kwargs):
        self.kwargs = {k:v for k,v in kwargs.items()}

    def start_servers(self):
        for func in [self.start_action, self.start_nlu]:
            t = threading.Thread(target=func)
            t.start()

    def kill(self):
        """kill action and nlu server daemon processes

        """
        # TODO:
        pass

    def start_action(self):
        # python -m rasa_core_sdk.endpoint --actions actions
        with open('action_server.log', 'a') as f:
            cmd = ['python', '-m', 'rasa_core_sdk.endpoint', '--actions', 'actions']
            p = subprocess.Popen(cmd, stdout=f, stderr=f)

    def start_nlu(self):
        try:
            with open('nlu_server.log', 'a') as f:
                cmd = ['python', '-m', 'rasa_nlu.server', '--pre_load', 'nlu', '--path', 'models', '--debug']
                p = subprocess.Popen(cmd, stdout=f, stderr=f)
        except Exception as e:
            print(e)

    # this code is buggy -- DON'T USE
    """
    def start_interactive_learning(self):
        cmd = ['python', '-m', 'rasa_core.train', 'interactive', '--core', 'models/dialogue', '--nlu', 'default/nlu', '--endpoints', 'config/endpoints.yml']
        p = subprocess.Popen(cmd)

    def run_bot(self):
        cmd = 'python -m rasa_core.run --core models/dialogue --nlu default/nlu --endpoints config/endpoints.yml'
        # cmd = ['/Users/asoa/.pyenv/shims/python', '-m', 'rasa_core.run', '--core', 'models/dialogue', '--nlu', 'default/nlu', '--endpoints', 'config/endpoints.yml']
        # p = subprocess.Popen(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE)

        with subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE, universal_newlines=True) as p, StringIO() as buf:
            for line in p.stdout:
                if line is not '':
                    print(line, end='')
    """

    def parse_arg(self):
        parser = argparse.ArgumentParser(usage='python -m server.init [[--start_action], [--start_nlu], [--kill]]',
                                         description='utility script to start/kill action server or nlu server')
        parser.add_argument('--start_action', dest='start_action', action='store_true', help='start the action server')
        parser.add_argument('--start_nlu', dest='start_nlu', action='store_true', help='start the nlu server')
        parser.add_argument('--kill', dest='kill', action='store_true', help='kill both action and nlu servers')
        args = parser.parse_args()

        if args.start_action:
            self.start_servers()
        elif args.start_nlu:
            self.start_nlu_server()
        elif args.start_action:
            self.start_action()
        elif args.kill:
            self.kill()
        else:
            print(parser.usage)

def main():
    s = Server().parse_arg()
    # print("Action server and NLU sever stopped")


if __name__ == "__main__":
    main()