import os
import base64
import openai

client = openai.OpenAI(
  base_url="https://qwen2-72b.lepton.run/api/v1/",
  api_key="6XN3K2Ydd7kroaDiBE3r0a9KZJWO0suZ"
)

format_ = "opus"
bitrate = 16
asr_input = "audio.mp3"

with open(asr_input, "rb") as f:
    audio_bytes = f.read()
    audio_data = base64.b64encode(audio_bytes).decode()

# calls the api
completion = client.chat.completions.create(
  model="qwen2-72b",
  # This specifies what audio input and output should be
  extra_body={
    # input formats
    "tts_audio_format": format_,
    "tts_audio_bitrate": bitrate,
    # output formats
    "require_audio": True,
    "tts_preset_id": "jessica",
  },
  # this gets you audio input
  messages=[
      {"role": "user", "content": [{"type": "audio", "data": audio_data}]}
  ],
  max_tokens=128,
  stream=True,
)

# Get both text and audios
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