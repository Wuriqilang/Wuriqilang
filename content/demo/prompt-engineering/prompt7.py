import openai
import os
from dotenv import load_dotenv,find_dotenv

_ = load_dotenv(find_dotenv()) # read local .env file

openai.api_key = os.getenv("OPENAI_API_KEY")

def get_completion(prompt, model = "gpt-3.5-turbo",temperature=0):
  messages = [{"role":"user","content":prompt}]
  response = openai.ChatCompletion.create(
    model=model,
    messages=messages,
    temperature=temperature,
  )
  return response.choices[0].message["content"]


# 情感
sentiment = "骄傲"

# 语料
doc = """
这次我参加作文比赛要求以爸爸为主题写一篇作文
我有一个区长父亲
他每天很忙很忙
"""

prompt = f"""
你是一名小学生, 
你的任务是根据给定的语料写一篇作文,文章题目是:我的区长父亲

语料内容通过三个反引号分隔.
这篇作文的情感是{sentiment}

语料内容:```{doc}```

"""


response = get_completion(prompt,temperature=0.7)
print(response)





