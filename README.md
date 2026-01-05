This is a **perfect first AI project** 
 **step by step**, from concept → setup → simple working app → improvements. Do **not** need advanced AI knowledge to start.

---

# Goal (What we are Building)

A simple AI app that:

1. Takes a **Google Review comment** as input
2. Uses an **AI model** to generate a
   👉 *friendly, professional business response*
3. Outputs the response for you to copy & post

We’ll start **manual input** (copy-paste reviews).

---

# High-Level Architecture (Simple Version)

```
Google Review (text)
        ↓
Your App (Python or JavaScript)
        ↓
AI Model (OpenAI API)
        ↓
Generated Professional Response
```

Tech Stack (Beginner-Friendly)

### Recommended (Simple & Popular)

* **Language:** Python
* **AI API:** OpenAI GPT model
* **Interface:** Command line 

Here’s a step-by-step explanation of the flow in app.py:
1.	Imports: The script imports necessary modules: os for environment variables, dotenv for loading .env files, a custom generate_prompt function from prompt.py, and the OpenAI client.
2.	Environment Setup: It loads environment variables from a .env file using load_dotenv(). It then retrieves the OpenAI API key from the environment and prints whether it was loaded successfully.
3.	OpenAI Client Initialization: The OpenAI API key is set for the openai library, and a new OpenAI client instance is created using this key.
4.	Response Generation Function: The generate_response function takes a Google review as input, generates a prompt using generate_prompt, and sends it to the OpenAI API (using the GPT-4.1-mini model). The AI’s response is returned as a string.
5.	Main Execution Block: If the script is run directly, it prompts the user to paste a Google review, generates an AI response using the above function, and prints the result.
Summary:
The script loads your OpenAI API key, takes a Google review as input, generates a prompt, sends it to OpenAI’s GPT-4.1-mini model, and prints the AI-generated response. The prompt generation logic is handled in prompt.py.
