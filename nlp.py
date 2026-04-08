from textblob import TextBlob

def analyze_text(text):
    blob = TextBlob(text)

    sentiment = blob.sentiment.polarity
    subjectivity = blob.sentiment.subjectivity
    word_count = len(text.split())
    sentence_count = len(blob.sentences)

    avg_sentence_length = word_count / sentence_count if sentence_count else 0

    return {
        "sentiment": sentiment,
        "subjectivity": subjectivity,
        "word_count": word_count,
        "sentence_count": sentence_count,
        "avg_sentence_length": avg_sentence_length
    }