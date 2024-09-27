import os
import openai

client = openai.OpenAI(
    base_url="https://qwen2-72b.lepton.run/api/v1/",
    api_key="6XN3K2Ydd7kroaDiBE3r0a9KZJWO0suZ",
)

completion = client.chat.completions.create(
    model="qwen2-72b",
    messages=[
        {"role": "user", "content": "can you tell me some thing about python?"},
    ],
    max_tokens=128,
    stream=True
)

for chunk in completion:
    if not chunk.choices:
        continue
    content = chunk.choices[0].delta.content
    print('===chunk===', chunk, end="\n")
    if content:
        print('', end="")