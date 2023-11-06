import streamlit as st
import openai

openai.api_key = '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'

# Define the function to get ChatGPT response
def get_gpt_response(user_input):
    response = openai.Completion.create(
        engine="davinci",
        prompt=f"You: {user_input}\nAI:",
        max_tokens=75,
        n=1,
        stop=["\n"]
    )
    return response.choices[0].text.strip()

# Set the title of the app
st.title("B.A.T.M.A.N_A.I")

# Initialize chat history
chat_history = []

# Create a chat interface
user_input = st.text_input("You:")
if st.button("Send"):
    user_message = f"You: {user_input}"
    chat_history.append(user_message)
    
    gpt_response = get_gpt_response(user_input)
    bot_message = f"B.A.T.M.A.N.A.I: {gpt_response}"
    chat_history.append(bot_message)

# Display chat history
st.text_area("Chat:", value="\n".join(chat_history), height=400000000)
