import openai
import os
from dotenv import load_dotenv,find_dotenv

_ = load_dotenv(find_dotenv()) # read local .env file

openai.api_key = os.getenv("OPENAI_API_KEY")

def get_completion(prompt, model = "gpt-3.5-turbo"):
  messages = [{"role":"user","content":prompt}]
  response = openai.ChatCompletion.create(
    model=model,
    messages=messages,
    temperature=0,
  )
  return response.choices[0].message["content"]


# 通用翻译器
# input = input("输入任何语言: ")

# prompt = f"""
# 请将以下文本分别翻译成中文、英语、法语和日语,并写成:
# 中文翻译: aaa,
# 英语翻译: xxx,
# 法语翻译: yyy,
# 日语翻译: zzz
# 的格式

# ```{input}```
# """


# 语气修整器
# doc = """
# 嗨,小老弟,你好吗?我是你的老朋友,今天天气不错,我们一起去打球吧!
# """

# prompt = f"""
# 请将以下文本转换成正式商务邮件语气:
# ```{doc}```
# """

# 格式转换
# data_json = { "学生名单" :[ 
#     {"name":"李白", "email":"libai@qq.com"},
#     {"name":"杜甫", "email":"dufu@qq.com"},
#     {"name":"王维", "email":"wangwei@qq.com"}
# ]}

# prompt = f"""
# 将以下Python字典从JSON转换为Markdown Table格式，保留表格标题和列名：{data_json}
# """

# response = get_completion(prompt)
# print(response)


# 语言矫正
text = [ 
  "The girl with the black and white puppies have a ball.",  # The girl has a ball.
  "Yolanda has her notebook.", # ok
  "Its going to be a long day. Does the car need it’s oil changed?",  # Homonyms
  "Their goes my freedom. There going to bring they’re suitcases.",  # Homonyms
  "Your going to need you’re notebook.",  # Homonyms
  "That medicine effects my ability to sleep. Have you heard of the butterfly affect?", # Homonyms
  "This phrase is to cherck chatGPT for spelling abilitty"  # spelling
]

for i in range(len(text)):
    prompt = f"""请校对并更正以下文本，无需输出原始文本，只输出纠正后的文本，且保持语种不变。
    如没有发现任何错误，请说“未发现错误”。
    
    例如：
    输入：I are happy.
    输出：I am happy.
    ```{text[i]}```"""
    response = get_completion(prompt)
    print(i, response)


