#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
from sklearn import metrics
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression

try:
    # py3
    from urllib.parse import unquote
except Exception as e:
    # py2
    from urlparse import unquote

# import matplotlib.pyplot as plt


def loadFile(name):
    filepath = os.path.join(os.getcwd(), name)
    with open(filepath, 'r') as f:
        data = f.readlines()
    # converting url encoded data to simple string
    return list(map(unquote, set(data)))


def main():
    badQueries = loadFile('badqueries.txt')
    validQueries = loadFile('goodqueries.txt')

    queries = badQueries + validQueries

    badCount = len(badQueries)
    validCount = len(validQueries)

    # labels, 1 for malicious and 0 for clean
    yBad = [1] * badCount
    yGood = [0] * validCount
    y = yBad + yGood

    # converting data to vectors
    vectorizer = TfidfVectorizer(
        min_df=0.0,
        analyzer="char",
        sublinear_tf=True,
        ngram_range=(1, 3)
    )
    X = vectorizer.fit_transform(queries)

    # splitting data
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    # class_weight='balanced'
    lgs = LogisticRegression(
        class_weight={1: 2 * validCount / badCount, 0: 1.0}
    )

    # training our model
    lgs.fit(X_train, y_train)

    # Evaluation
    predicted = lgs.predict(X_test)

    fpr, tpr, _ = metrics.roc_curve(y_test, (lgs.predict_proba(X_test)[:, 1]))
    auc = metrics.auc(fpr, tpr)

    print("Bad samples: %d" % badCount)
    print("Good samples: %d" % validCount)
    print("Baseline Constant negative: %.6f" % (validCount / (validCount + badCount)))
    print("------------")
    print("Accuracy: %f" % lgs.score(X_test, y_test))  # checking the accuracy
    print("Precision: %f" % metrics.precision_score(y_test, predicted))
    print("Recall: %f" % metrics.recall_score(y_test, predicted))
    print("F1-Score: %f" % metrics.f1_score(y_test, predicted))
    print("AUC: %f" % auc)


if __name__ == '__main__':
    main()
