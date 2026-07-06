from flask import Flask, render_template, request
import joblib
from sqlgen import generate_sql, extract_column

app = Flask(__name__)

model = joblib.load("sql_model.pkl")
vectorizer = joblib.load("vectorizer.pkl")


@app.route("/", methods=["GET", "POST"])
def home():

    result = ""

    if request.method == "POST":

        question = request.form["question"]

        question_vector = vectorizer.transform([question])

        prediction = model.predict(question_vector)[0]

        column = extract_column(question)

        result = generate_sql(question, prediction, column)

    return render_template("index.html", result=result)


if __name__ == "__main__":
    app.run(debug=True)