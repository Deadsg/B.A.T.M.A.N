import os
from openai import OpenAI

# Get your OpenAI API key from environment variable
api_key = os.getenv('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')

def predict(history, prompt):
    history_openai_format = []
    for human, assistant in history:
        history_openai_format.append({"role": "user", "content": human })
        history_openai_format.append({"role": "assistant", "content":assistant})

    client = OpenAI(api_key=api_key)
    response = client.chat.completions.create(
        messages=history_openai_format,
        model = "gpt-3.5-turbo-1106", 
        stream = True
    )

    partial_message = ""
    for chunk in response:
        text = (chunk.choices[0].delta.content)
        if text is not None:
            partial_message = partial_message + text
            yield partial_message

def main():
    history=[]  # Initialize history
    while True:
        user_input = input("You: ")
        if user_input.lower() in ['quit', 'exit']:
            break
        prompt = f"You: {user_input}\nAI:"
        reply = predict(history, prompt)
        print(f"AI: {reply}")

if __name__ == "__main__":
    main()