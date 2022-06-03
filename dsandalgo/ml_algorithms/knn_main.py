import numpy as np
from sklearn.datasets import load_iris
from knn import KNearestNeighbors
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
import pandas as pd

dataset = load_iris()

X = dataset.data
# X = np.random.uniform(1, 1000, (10, 4))
y = dataset.target
# y = np.random.choice(3, 10)

mu = np.mean(X, 0)
sigma = np.std(X, 0)
X = (X - mu) / sigma

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=45)

our_classifier = KNearestNeighbors(X_train, y_train, n_neighbors=3)
sklearn_classifier = KNeighborsClassifier(n_neighbors=3).fit(X_train, y_train)

our_accuracy = our_classifier.score(X_test, y_test)
sklearn_accuracy = sklearn_classifier.score(X_test, y_test)

print(pd.DataFrame([[our_accuracy, sklearn_accuracy]],
                   ['Accuracy'],
                   ['Our Implementation', 'Sklearn\'s Implementation']))
