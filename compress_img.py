from PIL import Image

def compress_image(input_image_path, output_image_path):
    with Image.open(input_image_path) as img:
        # 保存为 PNG 格式可以实现无损压缩，也可以根据需求保存为其他支持无损的格式如 TIFF 等
        img.save(output_image_path, "PNG", optimize=True)

compress_image("peng.png", "output.png")