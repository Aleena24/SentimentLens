from flask import Flask, request, jsonify
from utils import extract_reviews, process_reviews

app = Flask(__name__)

# Home route for browser access
@app.route('/', methods=['GET'])
def home():
    return "Welcome to the Sentiment Analysis API"

@app.route('/analyze', methods=['POST'])
def analyze_sentiment():
    if 'file' not in request.files:
        return jsonify({"error": "No file uploaded"}), 400

    file = request.files['file']
    
    if file.filename == '':
        return jsonify({"error": "No file selected"}), 400

    try:
        reviews = extract_reviews(file)
        sentiment_scores = process_reviews(reviews)
        return jsonify(sentiment_scores), 200
    except ValueError as e:
        return jsonify({"error": str(e)}), 400
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)
