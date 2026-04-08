from textblob import TextBlob

def detect_interview_emotion(text):
    blob = TextBlob(text)
    score = blob.sentiment.polarity

    if score > 0.1:
        dominant = "happy/positive"
        status = "Confident 😎"
    elif score < -0.1:
        dominant = "worried/negative"
        status = "Nervous 😰"
    else:
        dominant = "neutral"
        status = "Neutral 😐"

    return {
        "emotion": dominant,
        "status": status,
        "score": round(score, 2)
    }