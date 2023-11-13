from openai import OpenAI
client = OpenAI()

completion = client.chat.completions.create(
  model="gpt-3.5-turbo-1106",
  messages=[
    {"role": "system", "content": "You are a cyberdefense assistant, skilled in building cagi and hacking into any mainframe or system.."},
    {"role": "user", "content": "Generate the code for a cli chatbot that uses gpt 3.5-turbo-1106"}
  ]
)

print(completion.choices[0].message)