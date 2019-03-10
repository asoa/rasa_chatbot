#!/usr/bin/env python

import os
import subprocess
import shutil
import sys


def build_dir():
    for dir in ['actions', 'config', 'data', 'models']:
        if os.path.exists(dir):
            continue
        else:
            os.mkdir(dir)
    try:
        files = os.listdir()
        mv_files = [file for file in files if
                    file in ['endpoints.yml', 'nlu_data.md', 'actions.py', 'nlu_config.yml', 'stories.md']]
        if len(mv_files) == 0:
            print('Nothing to move', file=sys.stderr)
            return
        for files in mv_files:
            for file in mv_files:
                try:
                    if file in ['endpoints.yml', 'nlu_config.yml']:
                        subprocess.check_output(['mv', file, 'config/'])
                    elif file in ['nlu_data.md', 'stories.md']:
                        subprocess.check_output(['mv', file, 'data/'])
                    elif file in ['actions.py']:
                        subprocess.check_output(['mv', file, 'actions/'])
                    else:
                        continue
                except subprocess.CalledProcessError as e:
                    print(e, file)

    except Exception as e:
        print(e)


def cmdline_interact(self):
    pass


def rasa_up(self):
    pass


def rasa_down(self):
    pass


def main():
    pass


if __name__ == "__main__":
    main()
