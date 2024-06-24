from flask import Flask, request, jsonify
import joblib
from processData import preprocess_text

app = Flask(__name__)

with open('vietnamese-stopwords.txt', 'r', encoding='utf-8') as f:
    stopwords = set(f.read().splitlines())

category_models = joblib.load('category_models.pkl')
overall_model = joblib.load('overall_model.pkl')
overall_vectorizer = joblib.load('overall_vectorizer.pkl')

def get_topic_keywords(model, vectorizer, num_top_words=10):
    feature_names = vectorizer.get_feature_names_out()
    topics = []
    for topic_idx, topic in enumerate(model.components_):
        top_keywords = [feature_names[i] for i in topic.argsort()[:-num_top_words - 1:-1]]
        topics.append(top_keywords)
    return topics

@app.route('/analyze_category', methods=['POST'])
def analyze_category():
    data = request.json
    category = data['category']
    model, vectorizer = category_models.get(category, (None, None))
    if not model or not vectorizer:
        return jsonify({'error': 'Invalid category'}), 400

    texts = data['texts']
    processed_texts = [preprocess_text(text, stopwords) for text in texts]
    data_vectorized = vectorizer.transform(processed_texts)
    topics = model.transform(data_vectorized)

    response = []
    for topic_distribution in topics:
        top_topic_idx = topic_distribution.argmax()
        top_keywords = get_topic_keywords(model, vectorizer)[top_topic_idx]
        response.append(top_keywords)
    
    return jsonify({'topics': response})

@app.route('/predict_topic', methods=['POST'])
def predict_topic():
    data = request.json
    text = data['text']
    processed_text = preprocess_text(text, stopwords)
    data_vectorized = overall_vectorizer.transform([processed_text])
    topic_distribution = overall_model.transform(data_vectorized)
    top_topic_idx = topic_distribution.argmax()
    top_keywords = get_topic_keywords(overall_model, overall_vectorizer)[top_topic_idx]
    return jsonify({'topics': top_keywords})

if __name__ == '__main__':
    app.run(debug=True)