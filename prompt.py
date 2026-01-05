def generate_prompt(review_text):
    return f"""
You are a professional business owner responding to Google Reviews.

Write a friendly, polite, and professional response.

Rules:
- Be warm and appreciative
- Stay professional
- Do not be defensive
- Keep it short (2–4 sentences)

Customer Review:
"{review_text}"

Business Response:
"""