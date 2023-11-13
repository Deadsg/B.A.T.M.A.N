import os
from openai import Openai
client = OpenAI()

openai.api_key = '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'

def chat(message):
    completion = client.chat.completions.create(
    model="gpt-3.5-turbo",
    messages=[
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": message}
        ]
    )
    print['choices'][0]['message']['content']

while True:
    message = input("User: ")
    response = chat(message)
    print("Assistant: ", response)

class ChatBot:
    def __init__(self, api_key):
        self.api_key = api_key
        self.client = OpenAI(api_key=api_key)

    def predict(self, message, history):
        history_openai_format = []
        for human, assistant in history:
            history_openai_format.append({"role": "user", "content": human })
            history_openai_format.append({"role": "assistant", "content": assistant})
        history_openai_format.append({"role": "user", "content": message})

        response = self.client.chat.completions.create(
            messages=history_openai_format,
            model="gpt-3.5-turbo-1106", 
            stream=True
        )

        partial_message = ""
        for chunk in response:
            text = chunk.choices[0].delta.content
            if text is not None:
                partial_message = partial_message + text
                yield partial_message