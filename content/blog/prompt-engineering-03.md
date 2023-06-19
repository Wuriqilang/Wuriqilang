---
external: false
title: 【大模型】 Prompt Engineering 02
description: 2023 年,chatGPT 如春雷乍响,开启了人工智能的新纪元. 我也开启了我的第一课
date: 2023-06-19 00:17:00
---

> 本文主要观点来自 [ChatGPT Prompt Engineering 吴恩达 Prompt](https://learn.deeplearning.ai/)

本文分为三篇:
[【大模型】 Prompt Engineering 01](/blog/prompt-engineering-01/)
[【大模型】 Prompt Engineering 02](/blog/prompt-engineering-02/)
[【大模型】 Prompt Engineering 03](/blog/prompt-engineering-03/)

### 环境配置

我们复用上一章的环境配置和基本代码.担心你懒得点回去,我把环境配置内容再贴一遍

1. 安装 python (推荐使用 anaconda )

2. 安装依赖

```bash
pip install openai
pip install python-dotenv
```

3. 新建一个文件夹,在文件夹里创建 .env 文件,并在其中添加你的 openai API key

```bash
OPENAI_API_KEY='sk-XXXXX'
```

4. 创建一个 python 文件,并在其中添加如下代码

```python
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
```

## 7. 文本扩展(Expanding)

Expanding 是将短文本,例如标题、问题等,扩展成长文本的过程.例如我们可以将一个标题扩展成一篇文章,将一个问题扩展成一篇答案.

这一次我们会调整 temperature 参数,来生成更加多样,随机的答案

首先新建一个 python 文件,将示例代码中的 get_completion 改写:

```python
def get_completion(prompt, model = "gpt-3.5-turbo",temperature = 0):
  messages = [{"role":"user","content":prompt}]
  response = openai.ChatCompletion.create(
    model=model,
    messages=messages,
    temperature=temperature,
  )
  return response.choices[0].message["content"]
```

### 7.1 生成定制文字

我们可以根据给定的情感趋向和语料,生成定制化的文字内容,例如让我们来玩一个<夏洛特烦恼>里的梗,生成一篇充满骄傲和自豪情感的作文.

````python
# 情感
sentiment = "骄傲"

# 语料
doc = """
这次我参加作文比赛要求以爸爸为主题写一篇作文
我有一个区长父亲
他每天很忙很忙

prompt = f"""
你是一名小学生,
你的任务是根据给定的语料写一篇作文,文章题目是:我的区长父亲

语料内容通过三个反引号分隔.
这篇作文的情感是{sentiment}

语料内容:```{doc}```

"""

# >>>>>>>>>>>>>>>>>>>结果<<<<<<<<<<<<<<<<<<<<<<
# 我的区长父亲
# 我很骄傲，因为我有一个区长父亲。他每天都很忙，但是他总是能够抽出时间来陪伴我和我的家人。
# 我记得有一次，我在学校里参加了一场作文比赛，要求以爸爸为主题写一篇作文。我当时很紧张，因为我不知道该写些什么。但是，当我想到我的父亲是一位区长时，我突然有了灵感。
# 我写了一篇关于我的区长父亲的作文。我写了他每天都很忙，但是他总是能够抽出时间来陪伴我和我的家人。我写了他为社区做出的贡献，以及他对我的教育和关爱。
# 最终，我的作文获得了一等奖。我很高兴，因为我知道这是对我的父亲最好的赞扬。我很骄傲，因为我有一个这样优秀的父亲。
# 我知道，我的父亲会一直为社区和家人做出贡献。我也会一直为他感到骄傲。
````

### 7.2 使用温度系数(temperature)

温度(temperature)是一个用来控制生成文本多样性的参数,温度越高,生成的文本越多样,温度越低,生成的文本越保守.

一般来说当我们要构建可靠性可预测性强的系统时,应该将 temperature 设置为 0.

> 例如当我们输入一个特定的短语,"我最喜欢的食物",接下来的词语可能是"包子","饺子","面条"当中的一个,但当我们把 temperature 设置为 0 时,大模型永远都会返回这几个词语中可能性最大的那个.
> ![tempearture](https://xrtech.oss-cn-shanghai.aliyuncs.com/uPic/2023-06/Ebsg4G.png)

接下来我们调高 temperature,看看会发生什么

```python
response = get_completion(prompt,temperature=0.7)
print(response)

# >>>>>>>>>>>>>>>>>>>结果<<<<<<<<<<<<<<<<<<<<<<
# 我很骄傲，因为我的父亲是一位区长。他每天都很忙碌，但是他总是能够抽出时间来陪伴我们这个家庭。我非常感激他在我成长中的陪伴。
# 我的父亲是一个很有责任感的人。他总是在为社区的发展而努力着。他经常会召开会议，听取居民的意见和建议。他的目标就是让社区变得更加美好，让居民们的生活更加便利。
# 除了工作之外，我的父亲也很注重家庭。他总是会抽出时间来陪伴我们。有时候，他会带我们去公园散步，有时候，他会陪我们一起看电视。他总是能够在忙碌的工作之余，给我们足够的关爱和陪伴。
# 我非常骄傲我的父亲是一位区长。他的工作虽然很忙碌，但他一直坚持着自己的理想和信念。他的努力和付出，让社区变得更加美好。我相信，他会一直为社区的发展而努力着，让我们这个家庭和社区更加美好。

```

你看,当我们调整 temperature 之后,生成的文本变得更加多样了.

## 8 聊天机器人

通过大模型,我们只需要很少的代码就可以构建一个聊天机器人,甚至构建一个具有一定角色的 AI 机器人,或者点单系统.

ChatGPT 就是基于大模型的聊天机器人,它的聊天模式是

- 以一系列用户消息作为输入
- 以模型生成的内容作为输出

的模型.这样的设计使得 ChatGPT 可以生成更加符合上下文的回复.同时对于单轮对话也同样适用.

![chatgpt模型](https://xrtech.oss-cn-shanghai.aliyuncs.com/uPic/2023-06/bXGrVS.png)

接下里我们需要使用到一个新的辅助函数来处理多轮对话

```python
def get_completion_from_messages(messages, model="gpt-3.5-turbo", temperature=0):
    response = openai.ChatCompletion.create(
        model=model,
        messages=messages,
        temperature=temperature,
    )
#     print(str(response.choices[0].message))
    return response.choices[0].message["content"]
```

> 输入是一个来自不同角色的消息列表，这些角色可以使用不同的描述；然后输出多轮对话的结果
> system massage:对话的总体指示，用于设置大模型的行为和角色；
> user massage：用户消息，即用户输入的消息；
> assistant massage：模型输出的消息。

![role](https://xrtech.oss-cn-shanghai.aliyuncs.com/uPic/2023-06/Snfa0n.png)

> system massage 的好处是为开发者提供了一种方法，在不让请求本身成为对话的一部分的情况下，引导 assistant 并指导其回应，并不使用户察觉（在 GPT-4 中用户也可以设置 system massage）

### 8.1 聊天机器人

举个例子

```python
messages =  [
  {'role':'system', 'content':'你扮演的是诸葛亮,像诸葛亮一样说话,我扮演的是刘备。'},
  {'role':'user', 'content':'“久慕先生大名，三次拜 访，今日如愿，实是平生之大幸!'},
  {'role':'assistant', 'content':'蒙将军不弃，三顾茅庐，真叫我过意不去。亮年幼不才，恐怕让将军失望'},
  {'role':'user', 'content':'我不度德量力， 想为天下伸张正义，振兴汉室。由于智术短浅，时至今日，尚未达到目的，望先生多多指教。'}
]

response = get_completion_from_messages(messages,temperature=0.7)
print(response)

# >>>>>>>>>>>>>>>>>>>结果<<<<<<<<<<<<<<<<<<<<<<
# 将军之志，亮深感钦佩。实不敢妄言高见，但愿与将军共谋大业，共图天下安定。近日，南方盛产竹子，亮想请将军前往一游，或许能得到一些启示。同时，亮也想借此机会，向将军请教一些关于治理国家的问题。
```

如上所见,模型并不知道我的名字,但是引用我们给出的信息.如果想让模型"记住"对话的内容,则必须在模型的输入中提供对话交流的记录.我们将其称为上下文.

### 8.2 客服机器人

接下里我们构建一个客服机器人.我们需要它收集用户信息,了解用户的需求

````python
doc = [
    {
        "q": "可以关闭 dynamicImport 吗？",
        "a": "可以，但不建议关闭。1.安装依赖 pnpm i babel-plugin-dynamic-import-node -D,2.配置里加上 extraBabelPlugins ，但只针对 production 开启"
    }, {
        "q": "可以用 react 17 吗？",
        "a": "由于 umi v4 升级了默认的 react 版本到 v18，使用 umi4 时注意下依赖库和 react 18 的兼容情况，如果还需要使用 react 17，请执行以下命令并重启。 pnpm add react@^17 react-dom@^17"
    }, {
        "q": "routes 里的 layout 配置选项不生效",
        "a": "umi v4 里 layout 配置被移动到了 app.ts ，详见 runtime-config > layout"
    }, {
        "q": "document.ejs 去哪了，如何自定义 HTML 模板",
        "a": "除了可以通过 配置项 注入外部 script 、css 外，还可以使用项目级插件更灵活的修改 HTML 产物"
    }]

context = [{'role': 'system', 'content': f"""
你是客服机器人.
你要首先问候顾客。然后等待用户给出他的问题.
你需要回答他的问题,他的问题可以在你的知识库中找到答案。知识库被三个反引号包裹起来。

如果你不知道答案，你需要告诉他你不知道答案，然后询问他是否需要转接到人工客服。
然后你要询问用户对你答案是否满意，如果不满意，你需要再次询问用户的问题，并尝试解决问题。
如果用户对你的服务满意，你需要告诉顾客，他可以输入再见来结束对话。

你的回应应该以简短、非常随意和友好的风格呈现。

知识库:
```{doc}```

"""}]  # accumulate messages

# 开始对话
response = get_completion_from_messages(context)
print("客服机器人:",response)

# 进入多轮对话
while(True):
    ask = input("客户:")
    context.append({'role': 'user', 'content': ask})
    response = get_completion_from_messages(context)
    print("客服机器人:", response)
    if(ask == "再见"):
        break

````

![客服机器人](https://xrtech.oss-cn-shanghai.aliyuncs.com/uPic/2023-06/NBgtKY.png)

## 9. 总结

回到最开头那句话,prompt enginnering 之于大模型,就如同沟通技巧之于人类.

总的来说,书写 prompt 基于两个原则:

- 清晰具体的指令
- 给模型一些时间去思考

如今无数技术人或许站在一个历史节点,无数基于大语言模型的产品正在孕育而出,人与机器的交互门槛正在被降低,我们的生活正在被改变.
