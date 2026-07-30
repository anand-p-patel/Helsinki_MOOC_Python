#!/usr/bin/env python3

import numpy as np
import xml.etree.ElementTree as ET
from sklearn.naive_bayes import MultinomialNB
from sklearn.model_selection import cross_val_score, KFold

alphabet = "abcdefghijklmnopqrstuvwxyzäö-"

def load_finnish():
    filename = "src/kotus-sanalista_v1.xml"
    tree = ET.parse(filename)
    root = tree.getroot()
    return [s.text for s in root.findall(".//s") if s.text is not None]

def load_english():
    with open("src/words", encoding="utf-8") as data:
        return [line.rstrip() for line in data]

def get_features(a):
    X = np.zeros((len(a), len(alphabet)), dtype=int)
    for i, word in enumerate(a):
        for j, char in enumerate(alphabet):
            X[i, j] = word.count(char)
    return X

def contains_valid_chars(s):
    return set(s).issubset(set(alphabet))

def get_features_and_labels():
    finnish_raw = load_finnish()
    english_raw = load_english()

    finnish_cleaned = [
        w.lower() for w in finnish_raw
        if contains_valid_chars(w.lower())
    ]
    english_cleaned = [
        w.lower() for w in english_raw
        if not w[0].isupper() and contains_valid_chars(w.lower())
    ]

    words = np.array(finnish_cleaned + english_cleaned)
    y = np.array([0] * len(finnish_cleaned) + [1] * len(english_cleaned))
    X = get_features(words)
    return X, y

def word_classification():
    X, y = get_features_and_labels()
    model = MultinomialNB()

    cv = KFold(n_splits=5, shuffle=True, random_state=0)
    scores = cross_val_score(model, X, y, cv=cv)
    return scores

def main():
    print("Accuracy scores are:", word_classification())

if __name__ == "__main__":
    main()