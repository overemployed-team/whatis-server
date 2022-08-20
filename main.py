from flask import Flask, request, jsonify  
from flask_cors import CORS
import cohere
import os

app = Flask(__name__)
CORS(app, resources={r"/*": {"origins": "*"}})

@app.route('/what', methods=['POST'])
def what_is():
    content = request.json
    print(content)
    # TODO[]: get the question and tell the answer to response

    fake_response = [
        {
            "answer": "well, we didn't implement that yet."
        }
    ]
    return jsonify(fake_response)

if __name__ == "__main__":
    app.run(debug=True, host="api.whatisit.app", port=int(os.environ.get("PORT", 8080)))

