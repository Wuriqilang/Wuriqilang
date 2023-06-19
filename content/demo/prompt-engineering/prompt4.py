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




doc = """
《七步诗》
作者：曹植

煮豆燃豆萁，豆在釜中泣。
本是同根生，相煎何太急？
"""

prompt = f"""

从古诗识别以下项目:
- 古诗的标题
- 古诗的作者
- 古诗的中心思想
- 是否表达了愤怒?(是或否)

古诗用三个反引号分隔.

将你的返回格式化以"标题","作者","主题","愤怒"为key的JOSN对象
如果信息不存在,请使用"null"代替
将愤怒的值格式化为布尔值

答案尽可能简短


古诗：```{doc}```
"""

response = get_completion(prompt)
print(response)

