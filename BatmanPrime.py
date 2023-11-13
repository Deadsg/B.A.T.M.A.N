import os
import openai

openai.api_key = os.environ["OPENAI_API_KEY"]

response = openai.ChatCompletion.create(
              model="MODEL_NAME",
              messages=[{"role": "system", "content": 'SPECIFY HOW THE AI ASSISTANT SHOULD BEHAVE'},
                        {"role": "user", "content": 'SPECIFY WANT YOU WANT THE AI ASSISTANT TO SAY'}
              ])