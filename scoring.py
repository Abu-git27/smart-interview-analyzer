def calculate_score(nlp, emotion):
    score = 0

    # Answer Quality (50%)
    if nlp["word_count"] > 30:
        score += 50
    elif nlp["word_count"] > 15:
        score += 30
    else:
        score += 15

    # Confidence (30%)
    score += int(emotion["confidence_score"] * 30)

    # Communication (20%)
    if nlp["avg_sentence_length"] > 8:
        score += 20
    else:
        score += 10

    return score