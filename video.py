import os
import time
import requests
from leptonai.client import Client

api_token = '6XN3K2Ydd7kroaDiBE3r0a9KZJWO0suZ'
c = Client("https://svd.lepton.run", token=api_token)

task_id = c.run(
    seed=0,
    decode_chunk_size=8,
    fps=6,
    motion_bucket_id=127,
    noise_aug_strength=0.02,
    # base64 or url
    image="https://www.lepton.ai/playground/stable-video-diffusion/rocket.png"
)

print(f'Task ID: {task_id}')
retry = 0
while True:
    res = c.task.get(task_id=task_id)
    print('res=====>', res)
    if res.status_code != 200:
        print(res)
        retry += 1
        print(f'Failed to get task status, retry {retry}')
        if retry > 3:
            print("Failed to get task status")
            break
        time.sleep(10)
        continue
    task = res.json()
    if task['status'] == 'SUCCESS':
        print(task['result']['url'])
        video = requests.get(task['result']['url']).content
        with open('output_video.mp4', 'wb') as f:
            f.write(video)
        print("Video saved as output_video.mp4")
        break
    elif task['status'] == 'FAILED':
        print("Generate video failed")
        break
    else:
        print(".")
    time.sleep(10)

