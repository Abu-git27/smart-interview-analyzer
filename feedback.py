def generate_feedback(nlp, emotion, score):
    feedback = []

    if nlp["word_count"] < 20:
        feedback.append("Your answer is too short. Add more details.")

    if "Nervous" in emotion["status"]:
        feedback.append("Try to sound more confident.")

    if nlp["avg_sentence_length"] < 6:
        feedback.append("Improve sentence structure.")

    if score > 75:
        feedback.append("Excellent performance!")

    if not feedback:
        feedback.append("Good answer, keep improving!")

    return feedback