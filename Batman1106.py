from openai import OpenAI

api_key = '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'

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

def main():
    print("Chatbot: Hello! I am a CLI chatbot. You can start chatting with me. Type 'exit' to end the conversation.")

    message_history = []
    
    while True:
        user_input = input("You: ")

        if user_input.lower() == 'exit':
            print("Chatbot: Goodbye!")
            break

        response_generator = predict(user_input, message_history)
        for bot_response in response_generator:
            print("Bot:", bot_response)
            message_history.append((user_input, bot_response))
            break  # We only want the first response from the generator

if __name__ == "__main__":
    main()