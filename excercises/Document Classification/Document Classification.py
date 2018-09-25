import os

import numpy as np
from sklearn.externals import joblib
from sklearn.externals.joblib import Parallel
from sklearn.model_selection import train_test_split, cross_val_score, GridSearchCV
from sklearn.preprocessing import MaxAbsScaler
from sklearn.svm import SVC

np.random.seed(42)

if __name__ == '__main__':
    classification = 'classifier.mdl'
    file_name = "documentClassificationFile.npz"

    if os.path.exists(classification):
        text_clf = joblib.load(classification)

        n = int(input())
        text = []
        for _ in range(n):
            text.append(input().strip())
        text = np.array(text)

        print(*text_clf.predict(text), sep="\n")
    else:
        if os.path.exists(file_name):
            data = np.load(file_name)
            labels = data["labels"]
            text_data = data["text_data"]
        else:
            labels = []
            text_data = []
            with open("trainingdata.txt", "r") as file:
                file.readline()
                for line in file.readlines():
                    labels.append(int(line[:1]))
                    text_data.append(line[1:].strip())

            labels.extend([1, 4, 8])
            text_data.extend(["This is a document",
                              "this is another document",
                              "documents are seperated by newlines"])

            labels = np.array(labels)
            text_data = np.array(text_data)

            np.savez(file_name, labels=labels, text_data=text_data)

        from sklearn.feature_extraction.text import CountVectorizer, TfidfTransformer

        from sklearn.pipeline import Pipeline

        train, test, train_l, test_l = train_test_split(text_data, labels, train_size=.8, test_size=.2)

        # clf = SGDClassifier(loss='hinge', penalty='elasticnet',
        #                     alpha=0.01, random_state=42,
        #                     power_t=0.2222222222222222,
        #                     learning_rate='invscaling',
        #                     eta0=0.020202020202020204,
        #                     max_iter=1000, tol=None, shuffle=False, n_jobs=-1)
        clf = SVC(C=1, gamma=0.01, kernel='sigmoid')

        text_clf = Pipeline([
            ('vect', CountVectorizer(lowercase=False)),
            ('scaler', MaxAbsScaler()),
            ('tfidf', TfidfTransformer(norm=None)),
            ('clf', clf),
        ])

        # grid = GridSearchCV(text_clf, param_grid=dict(
        # tfidf__norm=['l1', 'l2', None],
        # tfidf__use_idf=[True, False],
        # tfidf__smooth_idf=[True, False],
        # tfidf__sublinear_tf=[True, False],
        # clf__loss=['hinge', 'log', 'modified_huber', 'squared_hinge', 'perceptron', 'squared_loss', 'huber',
        #            'epsilon_insensitive', 'squared_epsilon_insensitive'],
        # clf__penalty=['l1', 'l2', 'elasticnet', 'none'],
        # clf__learning_rate=['optimal', 'constant', 'invscaling'],
        # clf__alpha=np.linspace(1e-2, 1e-10, 500),
        # clf__eta0=np.linspace(.000000000000000000000000001, 1, 100),
        # clf__power_t=np.linspace(.000000000000000000000000001, 1, 10),
        # clf__n_jobs=[-1]
        # clf__max_iter=[1000]
        # ), verbose=10, n_jobs=-1)

        clf = SVC(C=1, gamma=0.01, kernel='sigmoid')
        grid = GridSearchCV(text_clf, dict(
            # clf__kernel=('rbf', 'linear', 'sigmoid'),
            # clf__C=(.01, .1, 1, 10.0, 100),
            # clf__gamma=['auto', .001, .0001, .01, .1, 1, 10, 100]
            clf__max_iter=np.arange(5, 100, 5)
        )
                            , n_jobs=-1, verbose=10)
        grid.fit(text_data, labels)
        print(grid.best_params_)
        print(grid.best_score_)
        joblib.dump(grid, "gridSearch.mdl")

        p = Parallel(-1)

        text_clf.fit(train, train_l)
        print(cross_val_score(text_clf, text_data, labels, cv=5, n_jobs=-1))
        joblib.dump(text_clf, "classifier.mdl")
