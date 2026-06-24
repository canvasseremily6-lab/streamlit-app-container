import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import MultinomialNB
from sklearn.pipeline import Pipeline
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics import accuracy_score, classification_report
import joblib

# Import movies csv & rename labels + features
movies = pd.read_csv('IMDB Dataset.csv')
X = movies['review']
y = movies['sentiment']

# train naives bayes classifier model w/pipeline
pipeline_model = Pipeline(steps = [
    ('vectorizer', TfidfVectorizer()),
     ('naives_bayes', MultinomialNB())
])

#fit model and dump into pkl file
pipeline_model.fit(X, y)
joblib.dump(pipeline_model,'sentiment_model.pkl')
