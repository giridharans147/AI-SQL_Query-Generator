import pandas as pd

from sklearn.feature_extraction.text import TfidfVectorizer

df= pd.read_csv("dataset.csv")

print(df.isnull().sum())

# Separate input and output

X = df["question"]

y = df["label"]

# Creating TF-IDF object
vectorizer = TfidfVectorizer()

# Convert text into numbers
X_vector = vectorizer.fit_transform(X)
print(X_vector)

print(X_vector.shape)

from sklearn.model_selection import train_test_split

X_train, X_test, y_train, y_test = train_test_split(
    X_vector,
    y,
    test_size=0.2,
    random_state=42
)

print("Training data:", X_train.shape)

print("Testing data:", X_test.shape)

#logistic regreesion
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score

log_model = LogisticRegression()


log_model.fit(X_train,y_train) 

print("Model trained successfully")

log_prediction = log_model.predict(X_test)
log_accuracy = accuracy_score(y_test,log_prediction)

print("log Accuracy:",log_accuracy)

#naive bayes
from sklearn.naive_bayes import MultinomialNB

nb_model = MultinomialNB()
nb_model.fit(X_train, y_train)
nb_prediction = nb_model.predict(X_test)
nb_accuracy = accuracy_score(y_test, nb_prediction)
print("Naive Bayes Accuracy:", nb_accuracy)

#knn
from sklearn.neighbors import KNeighborsClassifier

knn_model = KNeighborsClassifier(n_neighbors=5)
knn_model.fit(X_train, y_train)
knn_prediction = knn_model.predict(X_test)
knn_accuracy = accuracy_score(y_test, knn_prediction)
print("KNN Accuracy:", knn_accuracy)

#decision tree
from sklearn.tree import DecisionTreeClassifier

dt_model = DecisionTreeClassifier(random_state=42)
dt_model.fit(X_train, y_train)
dt_prediction = dt_model.predict(X_test)
dt_accuracy = accuracy_score(y_test, dt_prediction)
print("Decision Tree Accuracy:", dt_accuracy)

#random forest
from sklearn.ensemble import RandomForestClassifier

rf_model=RandomForestClassifier(n_estimators=200, random_state=42)
rf_model.fit(X_train, y_train)
rf_prediction = rf_model.predict(X_test)
rf_accuracy = accuracy_score(y_test, rf_prediction)
print("Random Forest Accuracy:", rf_accuracy)

# Compare all 5 models
results = {
    "Logistic Regression": log_accuracy,
    "Naive Bayes": nb_accuracy,
    "KNN": knn_accuracy,
    "Decision Tree": dt_accuracy,
    "Random Forest": rf_accuracy,
}

for name, acc in results.items():
    print(f"{name}: {acc:.4f}")

best_name = max(results, key=results.get)
print("Best model:", best_name)

models = {
    "Logistic Regression": log_model,
    "Naive Bayes": nb_model,
    "KNN": knn_model,
    "Decision Tree": dt_model,
    "Random Forest": rf_model,
}
best_model = models[best_name]

import joblib
joblib.dump(best_model, "sql_model.pkl")
joblib.dump(vectorizer, "vectorizer.pkl")

question = ["products price in descending order"]

question_vector = vectorizer.transform(question)

result = best_model.predict(question_vector)

print("Predicted Label:", result[0])