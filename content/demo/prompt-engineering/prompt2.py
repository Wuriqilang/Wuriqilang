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
概述

美丽的中世纪风格办公家具系列的一部分，包括文件柜、办公桌、书柜、会议桌等。
     多种外壳颜色和底座涂层可选。
     可选塑料前后靠背装饰（SWC-100）或 10 种面料和 6 种皮革的全面装饰（SWC-110）。
     底座涂层选项为：不锈钢、哑光黑色、光泽白色或铬。
     椅子可带或不带扶手。
     适用于家庭或商业场所。
     符合合同使用资格。

结构

五个轮子的塑料涂层铝底座。
     气动椅子调节，方便升降。

尺寸

宽度 53 厘米|20.87 英寸
     深度 51 厘米|20.08 英寸
     高度 80 厘米|31.50 英寸
     座椅高度 44 厘米|17.32 英寸
     座椅深度 41 厘米|16.14 英寸

选项

软地板或硬地板滚轮选项。
     两种座椅泡沫密度可选：中等（1.8 磅/立方英尺）或高（2.8 磅/立方英尺）。
     无扶手或 8 个位置 PU 扶手。

材料
外壳底座滑动件

改性尼龙 PA6/PA66 涂层的铸铝。
     外壳厚度：10 毫米。
     座椅
    HD36 泡沫

原产国

意大利
"""

# # 生成营销文案
# prompt = f"""
# 您的任务是帮助营销团队基于技术说明书创建一个产品的零售网站描述。

# 根据```标记的技术说明书中提供的信息，编写一个产品描述。

# 该描述面向家具零售商，因此应具有技术性质，并侧重于产品的材料构造。

# 在描述末尾，包括技术规格中每个7个字符的产品ID。

# 使用最多50个词。

# 技术规格：```{doc}```
# """


# 格式化输出
prompt = f"""
您的任务是帮助营销团队基于技术说明书创建一个产品的零售网站描述。

根据```标记的技术说明书中提供的信息，编写一个产品描述。

该描述面向家具零售商，因此应具有技术性质，并侧重于产品的材料构造。

在描述末尾，包括技术规格中每个7个字符的产品ID。

在描述之后，包括一个表格，提供产品的尺寸。表格应该有两列。第一列包括尺寸的名称。第二列只包括英寸的测量值。

给表格命名为“产品尺寸”。

将所有内容格式化为可用于网站的HTML格式。将描述放在<div>元素中。

技术规格：```{doc}```
"""

response = get_completion(prompt)
print(response)

