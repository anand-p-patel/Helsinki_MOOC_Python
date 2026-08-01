#!/usr/bin/env python3
import gzip
import numpy as np
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import MultinomialNB
from sklearn.metrics import accuracy_score

def spam_detection(random_state=0, fraction=1.0):
    with gzip.open("src/ham.txt.gz", "rt", encoding="utf-8", errors="ignore") as f:
        ham_lines = f.readlines()
    with gzip.open("src/spam.txt.gz", "rt", encoding="utf-8", errors="ignore") as f:
        spam_lines = f.readlines()

    ham_lines = ham_lines[:int(len(ham_lines)*fraction)]
    spam_lines = spam_lines[:int(len(spam_lines)*fraction)]
    texts = ham_lines + spam_lines

    y = np.array([0] * len(ham_lines) + [1] * len(spam_lines))

    vectorizer = CountVectorizer()
    X = vectorizer.fit_transform(texts)

    X_train, X_test, y_train, y_test = train_test_split(
        X, y, train_size=0.75, random_state=random_state
    )
    model = MultinomialNB()
    model.fit(X_train, y_train)

    y_pred = model.predict(X_test)

    acc = accuracy_score(y_test, y_pred)
    total_test = len(y_test)
    misclassified = int(np.sum(y_test != y_pred))

    return acc, total_test, misclassified
def main():
    accuracy, total, misclassified = spam_detection()
    print("Accuracy score:", accuracy)
    print(f"{misclassified} messages miclassified out of {total}")

if __name__ == "__main__":
    main()
