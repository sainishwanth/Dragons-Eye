import openai
import os

with open('openai_key', 'r') as file:
    secret_key = file.read()

openai.api_key = secret_key

print(f"key: {openai.api_key}")

def openai_generator(user_message, conversation_history):
    conversation_history.append({"role": "user", "content": user_message})
    completion = openai.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=conversation_history,
        temperature=0.7,
        max_tokens=150,
    )
    reply_content = completion.choices[0].message.content
    conversation_history.append({"role": "assistant", "content": reply_content})
    return reply_content, conversation_history