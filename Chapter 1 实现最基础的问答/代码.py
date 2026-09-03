from openai import OpenAI

client = OpenAI(
    api_key = "",
    base_url = "https://dashscope.aliyuncs.com/compatible-mode/v1"
    )
user_input = input("user:")
message = [
            {"role": "user", "content": user_input }
        ]
response = client.chat.completions.create(
    model = "qwen3.8-flash",
    messages = message
)

assistant_messages = response.choices[0].message.content
print(assistant_messages)