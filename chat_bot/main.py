#!/usr/bin/env python

from chat_bot import train

def main():
    # b = util.build_dir()
    t = train.Train(do_train_nlu=True)
    # t = train.Train(do_train_core=False)
    # t.predict_intent('hello, how are you')
    # t.train_interactive()


if __name__ == "__main__":
    main()
