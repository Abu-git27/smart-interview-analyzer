from flask import Flask, request, jsonify
from flask_cors import CORS
import os

from emotion import detect_interview_emotion
from scoring import calculate_score
from feedback import generate_feedback

# ✅ FIRST create app
app = Flask(__name__)
CORS(app)

@app.route('/')
def home():
    return "Backend is running!"

@app.route('/analyze', methods=['POST'])
def analyze():
    data = request.get_json()
    text = data.get('text', '')

    # NLP
    words = text.split()
    word_count = len(words)

    sentences = text.split('.')
    sentence_lengths = [len(s.split()) for s in sentences if s.strip()]
    avg_sentence_length = sum(sentence_lengths)/len(sentence_lengths) if sentence_lengths else 0

    nlp = {
        "word_count": word_count,
        "avg_sentence_length": avg_sentence_length
    }

    # Emotion
    emotion = detect_interview_emotion(text)
    confidence_score = (emotion["score"] + 1) / 2

    emotion_data = {
        "emotion": emotion["status"],
        "confidence_score": confidence_score
    }

    # Score
    score = calculate_score(nlp, emotion_data)

    # Feedback
    feedback = generate_feedback(nlp, emotion, score)

    return jsonify({
        "emotion_analysis": emotion,
        "final_score": {"total": score},
        "feedback": feedback
    })

# ✅ RUN AT LAST (VERY IMPORTANT)
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=int(os.environ.get("PORT", 5000)))