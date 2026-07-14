# Fake News Detection using Machine Learning

## About the Project

This is my Machine Learning project in which I built a web application to detect whether a news article is **Real** or **Fake**.

I first trained a machine learning model on a fake news dataset. After training the model, I saved it using `pickle` and connected it with a Flask web application. Users can paste any news article into the text box and click the **Predict** button to get the result.

This project helped me understand how a machine learning model can be used in a real web application.

---

## Technologies Used

* Python
* Flask
* Scikit-learn
* Pandas
* NumPy
* HTML
* CSS

---

## Project Structure

```text
Fake-News-Detection/
│
├── app.py
├── model.pkl
├── vectorizer.pkl
├── README.md
│
├── templates/
│   └── index.html
│
└── static/
    └── style.css
```

---

## How to Run the Project

1. Clone this repository.

```bash
git clone https://github.com/your-username/Fake-News-Detection.git
```

2. Install the required libraries.

```bash
pip install -r requirements.txt
```

3. Run the Flask application.

```bash
python app.py
```

4. Open your browser and go to:

```
http://127.0.0.1:5000
```

---

## Features

* Predicts whether a news article is Real or Fake.
* Simple and easy-to-use interface.
* Uses a trained machine learning model.
* Built with Flask.

---

## What I Learned

While making this project, I learned:

* Text preprocessing for machine learning.
* Training a classification model.
* Saving and loading models using Pickle.
* Connecting a machine learning model with Flask.
* Creating web pages using HTML and CSS.
* Handling user input through forms.

---

## Future Improvements

* Improve the user interface.
* Show prediction confidence.
* Deploy the application online.
* Try deep learning models like LSTM or BERT.

---

## Author

**Kajal**

B.Tech CSE (AI & ML)
