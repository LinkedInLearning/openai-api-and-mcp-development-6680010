import openai
import os

# Set your OpenAI API key (use environment variable for security)
api_key = os.getenv("OPENAI_API_KEY", "sk-...your-key-here...")

openai.api_key = api_key

response = openai.ChatCompletion.create(
    model="gpt-3.5-turbo",
    messages=[
        {"role": "system", "content": "You are a helpful assistant."},
        {"role": "user", "content": "Say hello!"}
    ]
)

print("AI Response:", response['choices'][0]['message']['content'])
