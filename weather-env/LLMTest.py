from openai import OpenAI
import os

def get_response():
    client = OpenAI(
        api_key=os.environ.get('DASH_SCOPE_API_KEY'),  # 请用阿里云百炼 API Key
        base_url="https://dashscope.aliyuncs.com/compatible-mode/v1",  # 填写DashScope SDK的base_url
    )
    completion = client.chat.completions.create(
        model="qwen-plus",
        messages=[
            {'role': 'system', 'content': 'You are a helpful assistant.'},
            {'role': 'user', 'content': '你是谁？'}
        ],
        stream=True,
        stream_options={"include_usage": True}
    )
    for chunk in completion:
        # chunk 里可能没有 choices 或 delta
        if hasattr(chunk, "choices") and len(chunk.choices) > 0:
            choice = chunk.choices[0]
            if hasattr(choice, "delta") and hasattr(choice.delta, "content"):
                print(choice.delta.content, end='', flush=True)

if __name__ == '__main__':
        get_response()

# import os
# from openai import OpenAI
#
# # 初始化客户端（核心配置：替换为你的API Key）
# client = OpenAI(
#     api_key=os.environ.get('DEEP_SEEK_API_KEY'),  # 推荐通过环境变量配置，也可直接写死（不推荐）
#     base_url="https://api.deepseek.com"  # DeepSeek 固定域名
# )
#
# # 调用对话API
# try:
#     response = client.chat.completions.create(
#         model="deepseek-chat",  # 指定模型，可选 deepseek-chat / deepseek-reasoner
#         messages=[
#             {"role": "system", "content": "You are a helpful assistant"},  # 系统角色定义
#             {"role": "user", "content": "Hello"},  # 用户提问
#         ],
#         stream=False  # 非流式输出（一次性返回完整结果）
#     )
#     # 打印回复内容
#     print("回复结果：", response.choices[0].message.content)
# except Exception as e:
#     print("调用失败：", str(e))