#!/usr/bin/env python

from chat_bot import train
from nlu import NLU

def main():
    n = NLU()
    n.train_nlu_docker()
    n.start_nlu_server()  # run to test intent classifier


if __name__ == "__main__":
    main()
