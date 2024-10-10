import os
from leptonai.client import Client

api_token = '6XN3K2Ydd7kroaDiBE3r0a9KZJWO0suZ'
c = Client("https://sdxl.lepton.run", token=api_token)

def generate_image():
    image = c.run(
        prompt="An anime girl who are playing basketball during a sunset",
        # prompt=prompt,
        height=1024,
        width=1024,
        guidance_scale=5,
        high_noise_frac=0.75,
        seed=1809774958,
        steps=30,
        use_refiner=False
    )
    with open('output_image1.png', 'wb') as f:
        f.write(image)
    print("Image saved as output_image.png", image)

generate_image()