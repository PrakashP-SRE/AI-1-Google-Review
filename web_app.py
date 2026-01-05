from flask import Flask, render_template, request
import os
from dotenv import load_dotenv
from prompt import generate_prompt
from openai import OpenAI

# Load environment variables from .env file
load_dotenv()

OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
client = OpenAI(api_key=OPENAI_API_KEY)

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    ai_response = None
    review = ''
    if request.method == 'POST':
        review = request.form['review']
        prompt = generate_prompt(review)
        response = client.chat.completions.create(
            model="gpt-4.1-mini",
            messages=[{"role": "user", "content": prompt}],
            temperature=0.7
        )
        ai_response = response.choices[0].message.content.strip()
    return render_template('index.html', ai_response=ai_response, review=review)

if __name__ == "__main__":
    app.run(debug=True)
