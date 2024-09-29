import os
import base64
import openai
import time
import json
from components.env import init_env
from connect_db_test import insert_audio
from components.spb import storage_client


import uuid
import datetime
current_time = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S');
current_timestamp = str(int(datetime.datetime.now().timestamp()) * 1000 )
# 生成一个随机的 UUID
random_uuid = str(uuid.uuid4())


init_env()

# hs
milliseconds = str(int(time.time() * 1000))

client = openai.OpenAI(
  base_url="https://llama3-1-405b.lepton.run/api/v1/",
  api_key=os.environ.get('LEPTON_API_KEY')
)

title='cat'
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
with open(random_uuid + '.mp3', 'wb') as f:
  f.write(buf)

# print("\nAudio saved to output.mp3")
# print('finalcontent===>', finalcontent)

with open(random_uuid + '.mp3', 'rb') as file:
    mp3_content = file.read()


bucket_name = 'resource-online'
file_name = "file/" + current_timestamp + '/' + random_uuid + '.mp3'


response = storage_client.from_(bucket_name).upload(file_name, mp3_content, {
  'content-type': 'audio/mpeg',
})
print('response===>', json.loads(response))

insert_audio(title, finalcontent, '/' + file_name)
