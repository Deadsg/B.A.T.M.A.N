import os
import openai


os.environ['OPENAI_API_KEY']

def generate_chat_completion(prompt, model="gpt-3.5-turbo"):
    messages = [{"role": "system", "content": "You are a helpful assistant."}]
    messages.append({"role": "user", "content": prompt})

    response = openai.ChatCompletion.create(
        model=model,
        messages=messages,
    )

    return response.choices[0].message["content"]

def main():
    print("Batman AI CLI Interface")
    print("Type 'exit' to end the conversation.")

    while True:
        user_input = input("You: ")
        if user_input.lower() == "exit":
            break

        response = generate_chat_completion(user_input)
        print(f"Chatbot: {response}")

if __name__ == "__main__":
    main()
