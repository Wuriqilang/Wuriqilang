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
造势近一个月的阿根廷中国行进入最后的高潮。北京时间6月15日晚，顶着世界杯夺冠的光环，阿根廷队在队长梅西的带领下，与澳大利亚进行的国际友谊赛在北京工人体育场拉开序幕。

据了解，这是足球巨星梅西的第八次中国行，不少球迷从各地来到北京，身着10号球衣表达对偶像的喜爱与支持。下午6时许，北京工人体育馆附近已是10号球衣的海洋！3岁半小球迷高喊口号：梅西梅西，梅西第一。

6月15日晚，北京新工人体育场，2023国际足球邀请赛开场仅81秒，梅西远射破门。最终，阿根廷队2-0完胜澳大利亚队。

当比赛终场哨声响起，整个“新工体”爆发出了雷鸣般的掌声。这热烈的欢呼不仅送给获胜的阿根廷队，也送给陪伴无数球迷走过青春岁月的球王梅西。

“感谢中国球迷对我从未更改的爱，我们很高兴来到这里。”

当第八次中国行画上句号，梅西也将前往美国迈阿密踢球：“在取得了所有成就，终于夺得了我非常渴望的世界杯冠军之后，我也想追求其它的事，以及内心的平静。”
"""

prompt = f"""

判断主题列表中的每一项是否是给定文本中的一个主题，

每个主题答案用 0 或 1表示，并以键值对的形式给出。

主题列表：比赛, 梅西

给定文本：```{doc}```
"""

response = get_completion(prompt)
print(response)

