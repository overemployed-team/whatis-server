from flask import Flask, request, jsonify  
from flask_cors import CORS
import cohere
import os
import pandas as pd
from difflib import SequenceMatcher

app = Flask(__name__)
CORS(app, resources={r"/*": {"origins": "*"}})
API_KEY = os.environ.get('API_KEY','')
co = cohere.Client(API_KEY)


def what_prompt(user_prompt):
    # read init phrase, readilng from what_init.txt
    with open('what_init.txt', 'r') as f:
        init_phrase = str(f.read())
    return init_phrase+user_prompt['question']+'\nWhat is it?\nA:'


def what_answer(prompt):
    generation = co.generate(
        model='xlarge',
        prompt= prompt,
        max_tokens=200,
        temperature=1,
        stop_sequences=["--",":"],
        k=0,
        p=0.75
        )
    return generation.generations[0].text.replace('\n--','').strip()


@app.route('/what', methods=['POST'])
def what_is():
    content = request.json
    prompt = what_prompt(content)    
    response = [
        {
            "answer": what_answer(prompt)
        }
    ]
    return jsonify(response)


@app.route('/generate', methods=['GET'])
def movie_generate():
    df = pd.read_csv('tmdb_5000_movies_clean.csv')
    # Get random row preferrly to popular
    row = df.sample(n=1, weights=df['antipop'])
    print()
    print(row.iloc()[0].overview)
    response = [
        {
            "title": row.iloc()[0].title,
            "description": row.iloc()[0].overview
        }
    ]
    return jsonify(response)


def similar(a, b):
    return SequenceMatcher(None, a, b).ratio()


@app.route('/isSame', methods=['POST'])
def is_same():
    content = request.json    
    original = content['original']
    users_guess = content['user']
    response = [
        {
            "is_same": True if similar(original, users_guess)>0.5 else False
        }
    ]
    return jsonify(response)


if __name__ == "__main__":
    app.run(
        debug=True,
        host=os.environ.get("HOST", "api.whatisit.app"),
        port=int(os.environ.get("PORT", 8080))
        )
