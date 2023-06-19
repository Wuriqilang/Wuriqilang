import openai
import os
from dotenv import load_dotenv, find_dotenv

_ = load_dotenv(find_dotenv())  # read local .env file

openai.api_key = os.getenv("OPENAI_API_KEY")


def get_completion_from_messages(messages, model="gpt-3.5-turbo", temperature=0):
    response = openai.ChatCompletion.create(
        model=model,
        messages=messages,
        temperature=temperature,
    )
    return response.choices[0].message["content"]

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
