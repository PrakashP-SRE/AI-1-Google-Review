def generate_prompt(review_text):
    # Simple sentiment detection (can be improved with ML/NLP)
    positive_keywords = ["good", "great", "excellent", "amazing", "wonderful", "love", "happy", "satisfied", "awesome", "fantastic", "best", "perfect", "recommend"]
    negative_keywords = ["bad", "poor", "terrible", "awful", "worst", "disappointed", "unhappy", "horrible", "problem", "issue", "rude", "not recommend", "never"]

    review_lower = review_text.lower()
    if any(word in review_lower for word in positive_keywords):
        rule = "The review is positive. Express gratitude."
    elif any(word in review_lower for word in negative_keywords):
        rule = "The review is negative. Apologize and offer resolution."
    else:
        rule = "The review is neutral. Acknowledge and reassure."

    return f"""
You are a professional business owner responding to Google Reviews.

Write a friendly, polite, and professional response.

Rules:
- If review is positive → express gratitude
- If review is neutral → acknowledge and reassure
- If review is negative → apologize and offer resolution
- Be warm and appreciative
- Stay professional
- Do not be defensive
- Keep it short (2–4 sentences)

Customer Review:
"{review_text}"

{rule}

Business Response:
"""