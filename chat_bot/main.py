#!/usr/bin/env python

from chat_bot import train
from chat_bot import util


def main():
    b = util.build_dir()
    # t = train.Train(do_train=False)
    t = train.Train(do_train=True)
    # t.predict_intent('hello how are you')


if __name__ == "__main__":
    main()
