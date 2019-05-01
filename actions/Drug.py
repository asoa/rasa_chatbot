#!/usr/bin/env python

from collections import defaultdict

import bs4
from bs4 import BeautifulSoup
import pickle
import requests
import re
import nltk
from nltk.stem import SnowballStemmer
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
        self.med_synthetic_dict = {'vicodin': ['hydrocodone'],
                                   'simvastatin': ['zocor'],
                                   'lisinopril': ['prinivil', 'zestril'],
                                   'levothyroxine': ['synthroid'],
                                   'azithromycin': ['zithromax', 'z-pak'],
                                   'metformin': ['glucophage'],
                                   'lipitor': ['atorvastatin'],
                                   'amlodipine': ['norvasc'],
                                   'amoxicillin': ['NULL'],
                                   'hydrochlorothiazide': ['hctz', 'water pill']}

        # initialize drug dictionary and pickle to disk
        if self.kwargs.get('train'):
            symptoms, labels = self.load_data()
            self.create_classifier(symptoms, labels)

        if self.kwargs.get('drug_init', False):
            self.parse_html()

        if self.kwargs.get('symptoms'):
            pp = self.pre_process(self.kwargs.get('symptoms'))
            self.pred = self.nb_predict(pp)
            print(self.pred)

    def init_drugs(self):
        """ initialize drug dictionary and pickle to disk """
        pass

    def load_data(self):
        print('***** generating classifier from pickled data *****')
        with open('drug_side_effects.pkl', 'rb') as f:  # load drug side effects from disk
            d = pickle.load(f)
        data = {}
        for drug, symptoms in d.items():
            drug_symptoms = [self.pre_process(symptom) for symptom in symptoms]  # preprocess the drug data

            flattened_symptoms = [item for l in drug_symptoms for item in l if item != '.']
            data[drug] = flattened_symptoms
        symptom_documents = [v for k, v in data.items()]
        symptom_labels = [k for k, v in data.items()]
        return symptom_documents, symptom_labels
        # self.create_classifier(symptom_documents, symptom_labels)  # data and labels to train the nb model

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
            print('***** updated drug database *****')
            pickle.dump(self.drug_side_effects, f)

    def stem(self, words):
        porter = SnowballStemmer('english')
        stem_words = set([porter.stem(word) for word in words])
        return stem_words

    def pre_process(self, text):
        """ remove irrelevant strings and stem words """
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

        _tokens = nltk.word_tokenize(replacement_string)
        tokens = self.stem(_tokens)
        if self.kwargs.get('debug', False):
            print(tokens)
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
        # self.clf.fit(array, labels)
        self.clf.fit(train_x, train_y)
        self.c_vocab = vectorizer.get_feature_names()
        pred = self.clf.predict(test_x)
        print(classification_report(test_y, pred))
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

        pred = clf.predict(_array)
        self.generics = self.med_synthetic_dict[pred[0]]
        print(pred, self.generics)

        fmt = '{:<20}{}'
        probs = clf.predict_proba(_array).tolist()
        # probs = [x for x in pred[0].split(' ')]
        i = 0
        for label in clf.classes_.tolist():
            print(fmt.format(label, probs[0][i]))
            i+=1

        return pred[0], self.generics




def main():
    # d_class = Drug(drug_init=False, train=True, debug=True)

    # d_class = Drug(symptoms="i've been having alot of joint pain, stuffy nose, and my throat is really sore", drug_init=False, debug=True)  # create instance of drug class
    # d_class = Drug(symptoms="i've been very weak,tired,loss of appetite lately, my pee is sometimes dark.  i'm also tired alot and i feel like i'm short of breath", drug_init=False, debug=True)  # create instance of drug class
    # d_class = Drug(symptoms="diarrhea, nausea, vomitting, stomach pain", drug_init=False, debug=True)  # create instance of drug class
    d_class = Drug(symptoms="My joints are really painful, my ankles swell sometimes", drug_init=False, debug=True)  # create instance of drug class


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
