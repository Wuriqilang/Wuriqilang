---
external: false
title: 【大模型】 Prompt Engineering 01
description: 2023 年,chatGPT 如春雷乍响,开启了人工智能的新纪元. 我也开启了我的第一课
date: 2023-06-18 00:17:00
---

> 本文主要观点来自 [ChatGPT Prompt Engineering 吴恩达 Prompt](https://learn.deeplearning.ai/)

## 1. 什么是 Prompt Engineering

大语言模型（LLM）在语料库上训练之后，并不能达到如 ChatGPT 那般令人惊艳的效果。本质上 LLM 的能力就是给定一段文字，进行续写。

- Base LLM: 基于大量数据训练的模型.
  当我们提问: "如何画一个圆?"
  模型会回答:
  ![如何画一个圆](https://xrtech.oss-cn-shanghai.aliyuncs.com/uPic/2023-06/8fS0aK.png)

- Instruction Tuned LLM:
  要让 LLM 显得更加智能，以人类能接受的方式生成回答，ChatGPT 用到了 RLHF (Reinforcement learning with human feedback) 的技术。经过 RLHF 微调的模型，我们叫做 Instruction Tuned LLM

举个例子:
在我们提问前,我们可以通过 prompt 来指导模型生成特定的文本.如:
![提示](https://xrtech.oss-cn-shanghai.aliyuncs.com/uPic/2023-06/Hml92u.png)

这时当我们提问: "如何画一个圆?"
模型就会在我们圈定的范围内给出合乎我们预期的答案.
![如何画一个圆](https://xrtech.oss-cn-shanghai.aliyuncs.com/uPic/2023-06/zE4C3m.png)

> 注 1：最早把强化学习引入语言模型中的，是 OpenAI 在 2019 年的一篇工作：Fine-Tuning Language Models from Human Preferences
> 注 2：RLHF 并不能有效提升模型的跑分，在小模型上性能甚至会有比较大的下降（随着参数增多，RLHF 微调会稍微增强性能），但是可以让它“显得”更智能

[InstructGPT (arxiv.org)](https://arxiv.org/pdf/2203.02155.pdf) 中详细介绍了 RLHF：
![RLHF](https://xrtech.oss-cn-shanghai.aliyuncs.com/uPic/2023-06/UQoq6h.jpg)

整个过程可以分成三步：

1. 通过人工写回答，收集了一个 prompt-response 数据集，用它对 GPT3 作微调，教会它如何产生人类想要的回答，得到的模型记作 fine-tuned GPT3。

2. 利用 fine-tuned GPT3 对某个 prompt 产生多个回答，并人工对它们按照好坏进行排序，可以称作 ranking 数据集。借助这些数据，训练一个 reward model，用来评估 response 的好坏，训练目标是尽量接近于人工排序。

3. 利用强化学习 PPO 算法，对 fine-tuned GPT3 进行优化。用强化学习中的术语来说， fine-tuned GPT3 就是 agent；Reward model 就是 environment，为 agent 的回答提供反馈。Agent 利用这个反馈优化自身参数，继续与环境交互，从而迭代优化。

> Note：相比于第二步中的 ranking 数据集，第一步中 prompt-response 数据集的收集代价更为昂贵（排序比自己写答案要简单太多了）。其实如果 prompt-response 数据集足够大，可以只用它在 GPT3 上做微调，而不需要强化学习。
> Note：1.3B（13 亿）参数量的 InstructGPT 产生的回答，效果要好于 175B 的 GPT-3

## 2.Prompt 编写原则

### 2.1 环境安装

本课程为实践课程,需要实机操作,既然是学习,咱们就一切从简,直接在也可以在本地搭建环境,
但是你也可以使用 [Google Colab](https://colab.research.google.com/),它可以免费使用 GPU,而且不需要配置环境,直接上手.

> 因为在访问 openai API 本来就需要科学上网,所这里我默认你已经具备了对应的网络条件.

1. 安装 python (推荐使用 anaconda )

2. 安装依赖

```bash
pip install openai
pip install python-dotenv
```

3. 创建 .env 文件,并在其中添加你的 openai API key

```bash
OPENAI_API_KEY='sk-XXXXX'
```

4. 创建 python 文件,并在其中添加如下代码

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

### 2.2 编写原则

#### 2.2.1 编写清晰、具体的指令

**策略 1**: 使用分隔符清晰地表示输入的不同部分
我们可以用任何明显的分隔符来将特定的文本与其余部分分开,分隔符可以是: ` ```，""，<>，，<\tag>` 等. 这么做可以有效避免提示注入.

> 提示注入: 提示注入是一种语言模型输入不符合预期的现象(也是一种用于劫持语言模型输出的技术)。当把用户输入文本作为提示的一部分使用时，就会发生这种情况。

举个例子: 我们使用 """ 作为分隔符
在上面的代码后面添加如下代码:

````python
text = f"""
你应该提供尽可能清晰、具体的指示，以表达你希望模型执行的任务。
这将引导模型朝向所需的输出，并降低收到无关或不正确响应的可能性。
不要将写清晰的提示与写简短的提示混淆。  
在许多情况下，更长的提示可以为模型提供更多的清晰度和上下文信息，从而导致更详细和相关的输出。
"""
# 需要总结的文本内容
prompt = f"""
把用三个反引号括起来的文本总结成一句话。
```{text}```
"""
# 指令内容，使用 ``` 来分隔指令和待总结的内容
response = get_completion(prompt)
print(response)
````

**策略 2** : 要求模型结构化输出
如要求模型使用 JSON 或 HTML,对象的形式输出,这样使模型结果更容易被解析
如下面例子

```python
prompt = f"""
请生成包括书名、作者和类别的三本虚构书籍清单，
并以 JSON 格式提供，其中包含以下键:book_id、title、author、genre。
"""
response = get_completion(prompt)
print(response)
```

**策略 3** 要求模型检查是否满足条件
如果我们需要模型执行的任务可能无法满足,我们可以要求模型检查是否满足条件,如果不满足,则返回错误信息. 这样我们就可以提前将潜在的边界情况考虑进去.

````python
text_1=f"""
泡一杯茶很容易。首先，需要把水烧开。
在等待期间，拿一个杯子并把茶包放进去。
一旦水足够热，就把它倒在茶包上。
等待一会儿，让茶叶浸泡。几分钟后，取出茶包。
如果你愿意，可以加一些糖或牛奶调味。
就这样，你可以享受一杯美味的茶了。
"""

prompt = f"""
您将获得由三个引号括起来的文本。
如果它包含一系列的指令，则需要按照以下格式重新编写这些指令：

第一步 - ... \n
第二步 - ...
...
第N步 - ...

如果文本中不包含一系列的指令，则直接写“未提供步骤”。"

\"\"\"{text_1}
\"\"\"
"""

# 指令内容，使用 ``` 来分隔指令和待总结的内容
response = get_completion(prompt)
print(response)



# >>>>>>> 输出 <<<<<<<
# Text 1 的总结:
# 第一步 - 把水烧开。
# 第二步 - 拿一个杯子并把茶包放进去。
# 第三步 - 把烧开的水倒在茶包上。
# 第四步 - 等待几分钟，让茶叶浸泡。
# 第五步 - 取出茶包。
# 第六步 - 如果你愿意，可以加一些糖或牛奶调味。
# 第七步 - 就这样，你可以享受一杯美味的茶了。

````

**策略 4** : 提供少量的示例
即在要求模型执行任务时,提供一些示例,这样可以帮助模型更好的理解我们的意图.

```python
prompt = f"""
你的任务是以一致的风格回答问题。

<孩子>: 教我耐心。

<祖父母>: 挖出最深峡谷的河流源于一处不起眼的泉眼；最宏伟的交响乐从单一的音符开始；最复杂的挂毯以一根孤独的线开始编织。

<孩子>: 教我韧性。
"""

# 最终输出的结果
# <祖父母>: 韧性就像是一棵树，它需要经历风吹雨打、寒冬酷暑，才能成长得更加坚强。所以，当你遇到挫折和困难时，不要轻易放弃，要像树一样坚定地扎根，不断成长，最终成为一棵高大的树。
```

#### 2.2.2 给模型时间去思考

**技巧一** : 技巧一：明确完成任务所需的步骤

下面的例子里，将任务分成了若干部分，让 LLM 分别完成

````python
text = f"""
李白乘舟将欲行, 忽闻岸上踏歌声。
桃花潭水深千尺, 不及汪伦送我情。
"""

作者：周末程序猿
链接：https://juejin.cn/post/7231519213893533754
来源：稀土掘金
著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。


prompt_1 = f"""
你的工作是:
1 - 一句话总结下面被三个反引号包裹的文本.
2 - 将总结翻译为法语
3 - 列出法语摘要中的每个名字
4 - 输出包含以下键的JSON对象: 法语摘要和名字数量统计

请用换行符分隔您的答案。

文本:
```{text}```
"""
````

最终返回
![结果](https://xrtech.oss-cn-shanghai.aliyuncs.com/uPic/2023-06/V2B9lH.png)

**技巧二** : 指导模型在下结论前找到自己的解法

有时候,告诉模型在下结论前要思考解决方案时,模型会给我们更好的回答.

```python

prompt = f"""
请判断学生的解决方案是否正确，请通过如下步骤解决这个问题：

步骤：

    首先，自己解决问题。
    然后将你的解决方案与学生的解决方案进行比较，并评估学生的解决方案是否正确。在自己完成问题之前，请勿决定学生的解决方案是否正确。

使用以下格式：

    问题：问题文本
    学生的解决方案：学生的解决方案文本
    实际解决方案和步骤：实际解决方案和步骤文本
    学生的解决方案和实际解决方案是否相同：是或否
    学生的成绩：正确或不正确

问题：
    我正在建造一个太阳能发电站，需要帮助计算财务。 
    - 土地费用为每平方英尺100美元
    - 我可以以每平方英尺250美元的价格购买太阳能电池板
    - 我已经谈判好了维护合同，每年需要支付固定的10万美元，并额外支付每平方英尺10美元
    作为平方英尺数的函数，首年运营的总费用是多少。

学生的解决方案：
    设x为发电站的大小，单位为平方英尺。
    费用：
    1. 土地费用：100x
    2. 太阳能电池板费用：250x
    3. 维护费用：100,000+100x
    总费用：100x+250x+100,000+100x=450x+100,000

实际解决方案和步骤：
"""
```

![方案](https://xrtech.oss-cn-shanghai.aliyuncs.com/uPic/2023-06/KTsNCc.png)
在上面例子中如果不加上提示,模型会直接认为学生解决方案时对的.

**技巧三** 让模型思考,减少虚假知识

虚假知识: 模型会一本正经的生成一些离题千里的答案.举个例子

```python
prompt = f"""
告诉我阿里云工业组态产品的特点和优势
"""
```

![虚假知识](https://xrtech.oss-cn-shanghai.aliyuncs.com/uPic/2023-06/Uk2iVD.png)

因为我参与了这个产品的研发,所以我很容易判断模型给出的答案是错误的.

这时候我们可以结合上面的技巧,让模型在下结论前思考,这样可以减少虚假知识的产生.一个有效的解决方案:

1. 找到相关的文献引用
2. 要求模型使用这些引用回答问题

```python
prompt = f"""
你的工作是:
1 - 查找关于阿里云组态产品的介绍文档,将他们列出来.
2 - 将列出来的文档总结成一句话.
3 - 结合总结,告诉我阿里云组态产品的特点
"""
```

![结果](https://xrtech.oss-cn-shanghai.aliyuncs.com/uPic/2023-06/u5gJKN.png)
