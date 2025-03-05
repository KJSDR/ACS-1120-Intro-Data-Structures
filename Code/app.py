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
    """Route that returns a web page styled like a tweet containing a generated sentence."""
    sentence = markov.generate_sentence(20)  # Generate a sentence of 20 words
    
    # HTML template for a tweet-like display
    html_content = f'''
    <html>
    <head>
        <style>
            body {{
                font-family: Arial, sans-serif;
                display: flex;
                justify-content: center;
                align-items: center;
                height: 100vh;
                background-color: #f5f8fa;
            }}
            .tweet-container {{
                background: white;
                padding: 20px;
                border-radius: 10px;
                width: 500px;
                box-shadow: 0px 4px 6px rgba(0, 0, 0, 0.1);
            }}
            .profile-pic {{
                width: 50px;
                height: 50px;
                border-radius: 50%;
                float: left;
                margin-right: 10px;
            }}
            .tweet-header {{
                display: flex;
                align-items: center;
            }}
            .user-name {{
                font-weight: bold;
                margin-right: 5px;
            }}
            .verified-badge {{
                width: 16px;
                height: 16px;
            }}
            .tweet-content {{
                margin-top: 10px;
                font-size: 16px;
            }}
        </style>
    </head>
    <body>
        <div class="tweet-container">
            <div class="tweet-header">
                <img class="profile-pic" src="https://upload.wikimedia.org/wikipedia/commons/thumb/1/16/%C3%89tienne_Carjat%2C_Portrait_of_Charles_Baudelaire%2C_circa_1862.jpg/800px-%C3%89tienne_Carjat%2C_Portrait_of_Charles_Baudelaire%2C_circa_1862.jpg" alt="Profile Picture">
                <span class="user-name">Charles Baudelaire</span>
                <img class="verified-badge" src="https://upload.wikimedia.org/wikipedia/commons/e/e4/Twitter_Verified_Badge.svg" alt="Verified">
            </div>
            <div class="tweet-content">
                {sentence}
            </div>
        </div>
    </body>
    </html>
    '''
    
    return html_content

if __name__ == "__main__":
    """To run the Flask server, execute `python app.py` in your terminal.
       To learn more about Flask's DEBUG mode, visit
       https://flask.palletsprojects.com/en/2.0.x/server/#in-code"""
    app.run(debug=True)