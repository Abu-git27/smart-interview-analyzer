import os

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=int(os.environ.get("PORT", 5000)))

    
from flask import Flask, request, jsonify
from flask_cors import CORS

from emotion import detect_interview_emotion
from scoring import calculate_score
from feedback import generate_feedback

app = Flask(__name__)
CORS(app)

@app.route('/')
def home():
    return "Backend is running!"

@app.route('/analyze', methods=['POST'])
def analyze():
    print("--- BUTTON CLICKED! MESSAGE RECEIVED ---")

    data = request.get_json()
    text = data.get('text', '')

    # ---------------- NLP ANALYSIS ----------------
    words = text.split()
    word_count = len(words)

    sentences = text.split('.')
    sentence_lengths = [len(s.split()) for s in sentences if s.strip() != ""]
    avg_sentence_length = sum(sentence_lengths)/len(sentence_lengths) if sentence_lengths else 0

    nlp = {
        "word_count": word_count,
        "avg_sentence_length": avg_sentence_length
    }

    # ---------------- EMOTION ----------------
    emotion = detect_interview_emotion(text)

    confidence_score = (emotion["score"] + 1) / 2

    emotion_data = {
        "emotion": emotion["status"],
        "confidence_score": confidence_score
    }

    # ---------------- SCORING ----------------
    score = calculate_score(nlp, emotion_data)

    # ---------------- FEEDBACK ----------------
    feedback = generate_feedback(nlp, emotion, score)

    return jsonify({
        "emotion_analysis": emotion,
        "nlp_analysis": nlp,
        "final_score": {
            "total": score
        },
        "feedback": feedback
    })

if __name__ == '__main__':
    app.run(host='127.0.0.1', port=5000, debug=True)