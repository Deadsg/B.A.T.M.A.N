import openai
import batman

# Set your OpenAI API key
openai.api_key = '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'

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

# Start the conversation
print("You can start chatting with the BATMAN_AI bot. Type 'exit' to end the conversation.")
while True:
    user_input = input("You: ")
    if user_input.lower() == 'exit':
        break

    prompt = f"You: {user_input}\nBATMAN_AI:"
    bot_response = generate_response(prompt)
    print(f"BATMAN_AI: {bot_response}")