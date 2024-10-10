from PIL import Image

def compress_and_resize_image(input_image_path, output_image_path, max_width, max_height):
    with Image.open(input_image_path) as img:
        width, height = img.size
        if width > max_width or height > max_height:
            ratio = min(max_width / width, max_height / height)
            new_width = int(width * ratio)
            new_height = int(height * ratio)
            img = img.resize((new_width, new_height), Image.LANCZOS)
        img.save(output_image_path, "PNG", optimize=True)
        
compress_and_resize_image("peng.png", "output2.png", 256, 256)