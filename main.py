from flask import Flask, request, jsonify  
from flask_cors import CORS
import cohere
import os

app = Flask(__name__)
CORS(app, resources={r"/*": {"origins": "*"}})
API_KEY = os.environ.get('API_KEY','')
co = cohere.Client(API_KEY)


def what_prompt(user_prompt):
    # read init phrase, readilng from what_init.txt
    with open('what_init.txt', 'r') as f:
        init_phrase = str(f.read())
    return init_phrase+user_prompt['question']+'\nWhat is it?\nA:'


def generate_answer(prompt):
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
    print(content)
    # TODO[]: get the question and tell the answer to response
    prompt = what_prompt(content)
    response = [
        {
            "answer": generate_answer(prompt)
        }
    ]
    return jsonify(response)

if __name__ == "__main__":
    app.run(
        debug=True,
        host=os.environ.get("HOST", "api.whatisit.app"),
        port=int(os.environ.get("PORT", 8080))
        )

