import streamlit as st
from openai import OpenAI
client = OpenAI(
    # defaults to os.environ.get("OPENAI_API_KEY")
    api_key="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",
)

def predict(history, message):
    history_openai_format = []
    for human, assistant in history:
        history_openai_format.append({"role": "system", "content": "You are a helpful assistant."})
        history_openai_format.append({"role": "user", "content": human })
        history_openai_format.append({"role": "assistant", "content":assistant})
    history_openai_format.append({"role": "user", "content": message})

generate_response = client.chat.completions.create(
    messages=[
        {
            "role": "user",
            "content": "",
        }
    ],
    model="gpt-3.5-turbo-1106",
)
def main():
    st.title("B.A.T.M.A.N_AI")

    # User input
    user_input = st.text_input("You:")

    if st.button("Ask"):
        if user_input:
            # Generate response from GPT-3.5 Turbo
            response = generate_response(user_input)
            st.write(f"Chatbot: {response}")
        else:
            st.warning("Please enter a question.")

if __name__ == "__main__":
    main()
