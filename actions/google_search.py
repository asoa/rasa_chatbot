#!/usr/bin/env python

from googlesearch import search
from bs4 import BeautifulSoup
from bs4.element import Comment
import urllib.request
import re
import nltk
from gensim.summarization.summarizer import summarize

class GoogleSearch:
    def __init__(self, **kwargs):
        self.kwargs = {k:v for k,v in kwargs.items()}
        self.user_query = self.kwargs.get('query')

    def g_search(self):
        pass


def main():
    pass

if __name__ == "__main__":
    main()
