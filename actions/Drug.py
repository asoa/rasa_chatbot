#!/usr/bin/env python

from collections import defaultdict

import bs4
from bs4 import BeautifulSoup
import pickle
import requests
import re
import nltk
import string
from nltk.corpus import stopwords
from nltk import BigramAssocMeasures  # bigram scorer
from nltk import BigramCollocationFinder  # used to get bigrams


class Drug:
    def __init__(self, *args, **kwargs):
        self.kwargs = {k:v for k,v in kwargs.items()}
        self.drugs = ['vicodin', 'simvastatin', 'lisinopril', 'levothyroxine', 'azithromycin', 'metformin', 'lipitor', 'amlodipine', 'amoxicillin', 'hydrochlorothiazide']
        self.drug_side_effects = defaultdict(list)
        self.url = 'https://www.drugs.com/'
        self.stopwords = [word for word in stopwords.words('english')]

    def init_drugs(self):
        """ initialize drug dictionary and pickle to disk """
        pass

    def parse_html(self):
        """ parses drug.com for side effects """
        # url = self.url + '/vicodin.html'
        for drug in self.drugs:
            upper_drug = drug[0].upper() + drug[1:]
            url = self.url + '/' + upper_drug + '.html'
            text = requests.get(url).text
            soup = BeautifulSoup(text, "html.parser")

            # start_text = '{} side effects'.format(upper_drug)
            start_parse = soup.find("h2", attrs={'id': 'sideEffects'})
            for sibling in start_parse.nextSiblingGenerator():
                if isinstance(sibling, bs4.NavigableString):
                    continue
                if isinstance(sibling, bs4.Tag) and 'interactions' in sibling.attrs.values():
                    break
                if isinstance(sibling, bs4.Tag):
                    # print(sibling.text)
                    self.drug_side_effects[drug].append(sibling.text.lstrip().rstrip())

        # write drug side effects to pickle object
        with open('drug_side_effects.pkl', 'wb') as f:
            pickle.dump(self.drug_side_effects, f)

    def pre_proces(self, text):
        """ remove irrelevant strings """
        replace_dict = {'Get emergency medical help if you have signs of an allergic reaction to \w+: ':'',
                        'This is not a complete list of side effects and others may occur. Call your doctor for medical advice about side effects. You may report side effects to FDA at 1-800-FDA-1088.':'',
                        }
        for pattern, replace in replace_dict.items():
            pass


    def tokenize(self, text):
        # tokens = [nltk.word_tokenize(sent) for sent in text]
        tokens = [word.lower() for sent in text for word in nltk.word_tokenize(sent)
                  if word not in string.punctuation and word not in self.stopwords]
        return tokens

    def get_bigrams(self, sents):
        """ generate bigrams to add to feature set
        - do this before removing puntuation and stop words

        """
        # remove punctuation
        for sent in sents:
            # _words = [word.lower() for word in sent if word not in string.punctuation]
            scorer = BigramAssocMeasures()
            bigrams = BigramCollocationFinder.from_words(sent.split())
            scored_bigrams = bigrams.score_ngrams(scorer.raw_freq)
            print([x for x in scored_bigrams])

    def vectorize(self):
        """ transform to vector representation if used in SVM """
        pass



def main():
    drug = Drug()
    with open('drug_side_effects.pkl', 'rb') as f:
        d = pickle.load(f)
    my_dict = defaultdict(list)
    for k,v in d.items():
        tokens = drug.tokenize(v)
        print(len(tokens))
        # my_dict[k].append(tokens)
    # print(my_dict)

if __name__ == "__main__":
    main()
