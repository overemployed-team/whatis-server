from flask import Flask, request, jsonify  
from flask_cors import CORS
import cohere

def create_app(test_config=None):
    print("Server started")
    app = Flask(__name__)
    CORS(app)

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

    return app

