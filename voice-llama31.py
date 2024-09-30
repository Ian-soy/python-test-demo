import os
import base64
import openai
import time
from image import generate_image

# hs
milliseconds = str(int(time.time() * 1000))

client = openai.OpenAI(
  base_url="https://llama3-1-405b.lepton.run/api/v1/",
  api_key="6XN3K2Ydd7kroaDiBE3r0a9KZJWO0suZ"
)

title='a beautiful girl'
lan="英语"
description = f"讲述一则关于{title}故事，要求120字左右，用词优美，随机生成的不同人物主题，不同故事情节，不需要故事总结，用{lan}输出"

# calls the api
completion = client.chat.completions.create(
  model="llama3-1-405b",
  # This specifies what audio input and output should be
  extra_body={
    # output formats
    "require_audio": True,
    "tts_preset_id": "lily",
  },
  # this gets you audio input
  messages=[
      {
        "role": "user", 
        "content": description
      }
  ],
  max_tokens=600,
  stream=True,
)

# Get both text and audios
audios = []
finalcontent = ""
for chunk in completion:
  if not chunk.choices:
    continue
  content = chunk.choices[0].delta.content
  audio = getattr(chunk.choices[0], 'audio', [])
  if content:
    finalcontent += content
    # print(content, end="")
  if audio:
    audios.extend(audio)

buf = b''.join([base64.b64decode(audio) for audio in audios[:]])
with open(milliseconds + '.mp3', 'wb') as f:
  f.write(buf)

print("\nAudio saved to output.mp3")
print('finalcontent===>', finalcontent)

generate_image(finalcontent)