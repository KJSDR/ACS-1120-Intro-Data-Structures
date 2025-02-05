"""Main script, uses other modules to generate sentences."""
from flask import Flask
from dictogram import Dictogram



app = Flask(__name__)

# TODO: Initialize your histogram, hash table, or markov chain here.
# Any code placed here will run only once, when the server starts.

word_list = "one fish two fish red fish blue fish".split()
histogram = Dictogram(word_list)


def generate_sentence(word_count=5):
    """Generate a sentence by randomly selecting weighted words."""
    return " ".join(histogram.sample() for _ in range(word_count))


@app.route("/")
def home():
    """Route that returns a web page containing the generated text."""
    sentence = generate_sentence()
    return f"<p>{sentence.capitalize()}.</p>"


if __name__ == "__main__":
    """To run the Flask server, execute `python app.py` in your terminal.
       To learn more about Flask's DEBUG mode, visit
       https://flask.palletsprojects.com/en/2.0.x/server/#in-code"""
    app.run(debug=True)
