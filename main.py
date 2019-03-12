#!/usr/bin/env python

import train

def main():
    t = train.Train(do_train_nlu=False, do_train_core=False)
    # t = train.Train(do_train_nlu=True, do_train_core=True)
    # t.predict_intent('hello, how are you')


if __name__ == "__main__":
    main()
