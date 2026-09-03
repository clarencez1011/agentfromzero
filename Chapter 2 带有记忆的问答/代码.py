from openai import OpenAI

client = OpenAI(
    api_key="真实使用的API Key",
    base_url="https://dashscope.aliyuncs.com/compatible-mode/v1",
)


def agent_loop():
    message = []
    while True:
        user_input = input("user:")
        if user_input == "exit":
            break
        #用户完成了写入，可以同步写入到消息列表中
        message.append(
            {"role": "user", "content": user_input}
        )

        response = client.chat.completions.create(
            model = "qwen3.8-flash",
            messages = message
        )
        assistant_messages = response.choices[0].message.content
        #此时已经获取了模型的返回，写入到消息列表中
        message.append(
            {"role": "assistant", "content": assistant_messages}
        )
        print(assistant_messages)
agent_loop()