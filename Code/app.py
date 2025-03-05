"""Main script, uses other modules to generate sentences."""
from flask import Flask, render_template
from .markov import MarkovChain
import random

app = Flask(__name__)

# TODO: Initialize your histogram, hash table, or markov chain here.
# Any code placed here will run only once, when the server starts.
markov = MarkovChain("Code/data/corpus.txt")

@app.route("/")
def home():
    """Route that returns a web page containing a generated sentence."""
    sentence = markov.generate_sentence(20)  # Generate a sentence of 20 words
    return f"<p>{sentence}</p>"

if __name__ == "__main__":
    """To run the Flask server, execute `python app.py` in your terminal.
       To learn more about Flask's DEBUG mode, visit
       https://flask.palletsprojects.com/en/2.0.x/server/#in-code"""
    app.run(debug=True)