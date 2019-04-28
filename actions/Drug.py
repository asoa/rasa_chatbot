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
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import GaussianNB, MultinomialNB
from sklearn.utils import resample
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report


class Drug:
    def __init__(self, *args, **kwargs):
        self.kwargs = {k:v for k,v in kwargs.items()}
        self.drugs = ['vicodin', 'simvastatin', 'lisinopril', 'levothyroxine', 'azithromycin', 'metformin', 'lipitor', 'amlodipine', 'amoxicillin', 'hydrochlorothiazide']
        self.drug_side_effects = defaultdict(list)
        self.url = 'https://www.drugs.com/'
        self.stopwords = [word for word in stopwords.words('english')]

        if self.kwargs.get('symptoms'):
            pp = self.pre_process(self.kwargs.get('symptoms'))
            self.pred = self.nb_predict(pp)
            print(self.pred)

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
                if isinstance(sibling, bs4.Tag):  # append drug side affects
                    # print(sibling.text)
                    self.drug_side_effects[drug].append(sibling.text.lstrip().rstrip())

        # write drug side effects to pickle object
        with open('drug_side_effects.pkl', 'wb') as f:
            pickle.dump(self.drug_side_effects, f)

    def pre_process(self, text):
        """ remove irrelevant strings """
        pattern = re.compile(r""" 
                ^Get\semergency.*
            |   ^Call\syour\sdoctor.*
            |   ^This\sis\snot\sa\scomplete\slist\sof\sside\seffects.*
            |   ^See also:\s.*
            |   '!"\#\$%&'\(\)\*\+,\./:;<=>\?@\[\\]\^_`{|}~
            |   :
            |   ,
            |   "
        """, re.VERBOSE)

        clean_text = pattern.sub('', text)
        punc_split_pattern = re.compile(r""";|--|-|\n\n|\n|\(|\)""")  # remove joined tokens such as word1-word2
        replacement_string = punc_split_pattern.sub(' ', clean_text)

        tokens = nltk.word_tokenize(replacement_string)
        return tokens

    def create_classifier(self, medicines, labels):
        """ generate bigrams to add to feature set
        - do this before removing punctuation and stop words

        """
        vectorizer = CountVectorizer(stop_words='english', ngram_range=(1,2))
        freq_matrix = vectorizer.fit_transform([' '.join(medicine) for medicine in medicines])
        array = freq_matrix.toarray()

        # create classifier
        X, y = resample(array, labels, n_samples=1000, random_state=155, replace=True)
        train_x, test_x, train_y, test_y = train_test_split(X, y, train_size=0.8, test_size=0.2, random_state=155)
        self.clf = MultinomialNB(alpha=1)
        # self.clf = GaussianNB()
        self.clf.fit(array, labels)
        self.c_vocab = vectorizer.get_feature_names()
        # pred = self.clf.predict(train_x)
        # print(classification_report(train_y, pred))
        with open('c_vocab', 'wb') as v:
            pickle.dump(self.c_vocab, v)
        with open('nb_model.pkl', 'wb') as f:
            pickle.dump(self.clf, f)

    def nb_predict(self, input_string):
        with open('c_vocab', 'rb') as v:
            c_vocab = pickle.load(v)
        with open('nb_model.pkl', 'rb') as f:
            clf = pickle.load(f)
        # array = self.pre_process(input_string)
        vectorizer = CountVectorizer(stop_words='english', ngram_range=(1, 2), vocabulary=c_vocab)
        freq_matrix = vectorizer.fit_transform([' '.join(input_string)])
        _array = freq_matrix.toarray()

        # pred = self.clf.predict_proba(_array)
        pred = clf.predict(_array)
        return pred


def main():
    d_class = Drug(symptoms="it burns when i urinate")  # create instance of drug class

    # create/train classifier

    # with open('drug_side_effects.pkl', 'rb') as f:  # load drug side effects from disk
    #     d = pickle.load(f)
    # data = {}
    # for drug, symptoms in d.items():
    #     drug_symptoms = [d_class.pre_process(symptom) for symptom in symptoms]  # preprocess the drug data
    #
    #     flattened_symptoms = [item for l in drug_symptoms for item in l if item != '.']
    #     data[drug] = flattened_symptoms
    # symptom_documents = [v for k, v in data.items()]
    # symptom_labels = [k for k, v in data.items()]
    # d_class.create_classifier(symptom_documents, symptom_labels)  # data and labels to train the nb model

    # predict

    # symptoms = "it burns when i urinate"
    # pp = d_class.pre_process(symptoms)
    # d_class.nb_predict(pp)


if __name__ == "__main__":
    main()
