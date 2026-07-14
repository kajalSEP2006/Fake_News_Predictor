from flask import Flask, render_template, request
import pickle

app = Flask(__name__)

# Load trained model and vectorizer
model = pickle.load(open("model.pkl", "rb"))
vectorizer = pickle.load(open("vectorizer.pkl", "rb"))


@app.route("/", methods=["GET", "POST"])
def home():

    prediction = ""
    news = ""

    if request.method == "POST":

        news = request.form["news"]

        # Convert text into numerical features
        news_vector = vectorizer.transform([news])

        # Predict
        result = model.predict(news_vector)

        if result[0] == 0:
            prediction = "🟢 REAL NEWS"
        else:
            prediction = "🔴 FAKE NEWS"

    return render_template(
        "index.html",
        prediction=prediction,
        news=news
    )


if __name__ == "__main__":
    app.run(debug=True)