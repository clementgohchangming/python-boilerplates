import pandas as pd
from sklearn.ensemble import RandomForestClassifier
import joblib


df = pd.read_csv("titanic.csv")

print(df.head())

encoded_ticker_class: pd.DataFrame = pd.get_dummies(df['ticket_class'], drop_first=True)
encoded_gender: pd.DataFrame = pd.get_dummies(df['gender'], drop_first=True)
df.drop('ticket_class', axis=1, inplace=True)
df.drop('gender', axis=1, inplace=True)
df = pd.concat([df, encoded_ticker_class, encoded_gender], axis=1)

x = df[df.columns.difference(['survived'])]

print(x.head())

y = df['survived']

classifier = RandomForestClassifier()
classifier.fit(x, y)

joblib.dump(classifier, '../titanic_model.pkl')