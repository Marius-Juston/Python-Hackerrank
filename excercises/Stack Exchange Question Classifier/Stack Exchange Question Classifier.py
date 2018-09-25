import json

from sklearn.externals import joblib
from sklearn.feature_extraction.text import CountVectorizer, TfidfTransformer
from sklearn.linear_model import SGDClassifier
from sklearn.model_selection import cross_val_score, GridSearchCV
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import LabelEncoder, Imputer

if __name__ == '__main__':

    with open("training.json", 'r', encoding='UTF-8') as file:

        n = int(file.readline())

        topic = []

        question = []
        excerpt = []

        for line in file.readlines():
            data = json.loads(line)
            topic.append(data['topic'].strip())
            question.append(data['question'].strip().lower())
            excerpt.append(data['excerpt'].strip().lower())
        label_encoder = LabelEncoder()
        labels = label_encoder.fit_transform(topic)

        # features = np.c_[question, excerpt]
        # features = np.unique(features, axis=0)

        import scipy.sparse as sp

        question_vectorizer = CountVectorizer()
        subject_vectors = question_vectorizer.fit_transform(question)

        excerpt_vectorizer = CountVectorizer()
        body_vectors = excerpt_vectorizer.fit_transform(excerpt)

        features = sp.hstack([subject_vectors, body_vectors], format='csr')

        # features = np.nan_to_num(features)

        # features = np.unique(features, axis=0)

        clf = SGDClassifier(
            loss='hinge', penalty='elasticnet',
            alpha=0.01, random_state=42,
            power_t=0.2222222222222222,
            learning_rate='invscaling',
            eta0=0.020202020202020204,
            max_iter=1000, tol=None, shuffle=False, n_jobs=-1)

        text_clf = Pipeline([

            # ('scaler', StandardScaler(with_mean=False)),
            ('fixer', Imputer(missing_values='NaN', strategy='mean', axis=0)),
            ('tfidf', TfidfTransformer(norm=None)),
            ('clf', clf)
        ])

        grid = GridSearchCV(text_clf, param_grid=dict(
            tfidf__norm=['l1', 'l2', None],
            tfidf__use_idf=[True, False],
            tfidf__smooth_idf=[True, False],
            tfidf__sublinear_tf=[True, False],
            # clf__loss=['hinge', 'log', 'modified_huber', 'squared_hinge', 'perceptron', 'squared_loss', 'huber',
            #            'epsilon_insensitive', 'squared_epsilon_insensitive'],
            # clf__penalty=['l1', 'l2', 'elasticnet', 'none'],
            # clf__learning_rate=['optimal', 'constant', 'invscaling'],
            # clf__alpha=np.linspace(1e-2, 1e-10, 500),
            # clf__eta0=np.linspace(.000000000000000000000000001, 1, 100),
            # clf__power_t=np.linspace(.000000000000000000000000001, 1, 10),
            # clf__n_jobs=[-1]
        ), verbose=10, n_jobs=-1)

        grid.fit(features, labels)
        print(grid.best_params_)
        print(grid.best_score_)
        joblib.dump(grid, "gridSearch.mdl")

        # clf.fit(combined_2, labels)
        val = cross_val_score(clf, features, labels, cv=3, n_jobs=-1)
        print(val)
        print(val.mean())
