import os
import base64
import openai

client = openai.OpenAI(
  base_url="https://qwen2-72b.lepton.run/api/v1/",
  api_key="6XN3K2Ydd7kroaDiBE3r0a9KZJWO0suZ"
)

# tell a compelete story about a cat near one minute

completion = client.chat.completions.create(
  model="qwen2-72b",
  messages=[
    {"role": "user", "content": "讲述一则幼儿寓言故事，要求150字左右，故事采用不一样的开头，不同场景，不同时间，不同地点，不同姓名，不同人物主题，不同故事情节，不需要故事总结，用英文输出"},
  ],
  max_tokens=256,
  stream=True,
  extra_body={
    "require_audio": "true",
    "tts_preset_id": "jessica",
  }
)

audios = []

for chunk in completion:
  if not chunk.choices:
    continue
  content = chunk.choices[0].delta.content
  audio = getattr(chunk.choices[0], 'audio', [])
  if content:
    print(content, end="")
  if audio:
    audios.extend(audio)

buf = b''.join([base64.b64decode(audio) for audio in audios[:]])

with open('output.mp3', 'wb') as f:
  f.write(buf)

print("\nAudio saved to output.mp3")
