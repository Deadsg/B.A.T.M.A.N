import openai

# Set up your OpenAI API key
openai.api_key = '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'

def process_command(command):
    if command.lower() == 'hello':
        return "Hello! How can I assist you?"
    elif command.lower() == 'goodbye':
        return "Goodbye! Have a great day!"
    elif command.lower() == 'generate_text':
        return generate_text()
    else:
        return "I'm sorry, I don't understand that command. Please try again."

def generate_response(prompt):
    response = openai.Completion.create(
        engine="text-davinci-003",  # Use GPT-3.5 Turbo engine
        prompt=prompt,
        max_tokens=150,  # Adjust as needed
        n=1,
        stop=None,
        temperature=0.6
    )
    return response.choices[0].text.strip()

# Example usage
user_command = input("Enter your command: ")
response = process_command(user_command)
print(response)

print("You can start chatting with the BATMAN_AI bot. Type 'exit' to end the conversation.")
while True:
    user_input = input("You: ")
    if user_input.lower() == 'exit':
        break

    prompt = f"You: {user_input}\nBATMAN_AI:"
    bot_response = generate_response(prompt)
    print(f"BATMAN_AI: {bot_response}")