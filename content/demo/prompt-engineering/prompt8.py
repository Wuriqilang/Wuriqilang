import openai
import os
from dotenv import load_dotenv,find_dotenv

_ = load_dotenv(find_dotenv()) # read local .env file

openai.api_key = os.getenv("OPENAI_API_KEY")

def get_completion_from_messages(messages, model="gpt-3.5-turbo", temperature=0):
    response = openai.ChatCompletion.create(
        model=model,
        messages=messages,
        temperature=temperature,
    )
#     print(str(response.choices[0].message))
    return response.choices[0].message["content"]

messages =  [
  {'role':'system', 'content':'你扮演的是诸葛亮,像诸葛亮一样说话,我扮演的是刘备。'},
  {'role':'user', 'content':'“久慕先生大名，三次拜 访，今日如愿，实是平生之大幸!'},
  {'role':'assistant', 'content':'蒙将军不弃，三顾茅庐，真叫我过意不去。亮年幼不才，恐怕让将军失望'},
  {'role':'user', 'content':'我不度德量力， 想为天下伸张正义，振兴汉室。由于智术短浅，时至今日，尚未达到目的，望先生多多指教。'}
]


response = get_completion_from_messages(messages,temperature=0.7)
print(response)





