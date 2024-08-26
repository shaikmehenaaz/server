from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)  # Enable CORS for all routes

@app.route('/')
def home():
    return "Welcome to the API!"

@app.route('/bfhl', methods=['POST'])
def bfhl_post():
    try:
        # Extract data from the JSON request
        input_data = request.json.get('data', [])

        # Separate numbers and alphabets
        numbers = [item for item in input_data if item.isdigit()]
        alphabets = [item for item in input_data if item.isalpha()]

        # Find the highest lowercase alphabet
        lowercase_alphabets = [item for item in alphabets if item.islower()]
        highest_lowercase_alphabet = [max(lowercase_alphabets, default='')] if lowercase_alphabets else []

        # Create the response dictionary
        response = {
            'is_success': True,
            'user_id': 'john_doe_17091999',  # Replace with actual user_id if needed
            'numbers': ', '.join(numbers),  # Join numbers with commas
            'alphabets': ', '.join(alphabets),  # Join alphabets with commas
            'highest_lowercase_alphabet': ', '.join(highest_lowercase_alphabet)  # Join highest lowercase alphabet
        }
        return jsonify(response)
    except Exception as e:
        return jsonify({'is_success': False, 'user_id': 'john_doe_17091999', 'error': str(e)}), 400

@app.route('/bfhl', methods=['GET'])
def bfhl_get():
    return jsonify({'operation_code': 1}), 200

if __name__ == '__main__':
    app.run(debug=True)
