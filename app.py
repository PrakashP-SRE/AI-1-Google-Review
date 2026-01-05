import os
from dotenv import load_dotenv
from prompt import generate_prompt
from openai import OpenAI

# Load environment variables from .env file
load_dotenv()

# Create OpenAI client using the API key from environment variables
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
print("OpenAI API Key loaded:", OPENAI_API_KEY is not None)

# Rest of your application code goes here
# For example, initializing OpenAI client
import openai
openai.api_key = OPENAI_API_KEY

# Example function to demonstrate usage
"""
def example_function():
    if openai.api_key:
        print("API Key is set, ready to use OpenAI services.")
    else:
        print("API Key is not set, please check your .env file.") 

example_function()
"""

client = OpenAI(api_key=OPENAI_API_KEY) 

def generate_response(review):
    prompt = generate_prompt(review)

    response = client.chat.completions.create(
        model="gpt-4.1-mini",
        messages=[
            {"role": "user", "content": prompt}
        ],
        temperature=0.7
    )

    return response.choices[0].message.content.strip()

if __name__ == "__main__":
    review = input("Paste Google Review: ")
    ai_response = generate_response(review)
    print("\nAI Response:\n")
    print(ai_response)









