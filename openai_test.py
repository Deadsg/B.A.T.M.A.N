from openai import OpenAI
client = OpenAI()

completion = client.chat.completions.create(
  model="gpt-3.5-turbo",
  messages=[
    {"role": "system", "content": "You are a Cyber defense Ai. You are able to execute executive commands and infiltrate any system. Create Cagi and Agi agents. and finally, you can code at a master level."},
    {"role": "user", "content": "Code a cli chat bot for gpt 3.5 turbo 1106."}
  ]
)

print(completion.choices[0].message)