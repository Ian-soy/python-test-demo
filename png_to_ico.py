from PIL import Image

def convert_png_to_ico(input_path, output_path, size=(128, 128)):
    img = Image.open(input_path)
    resized_img = img.resize(size)
    resized_img.save(output_path, format='ICO')

# 调用函数进行转换，假设输入文件是'input.png'，输出文件是'output.ico'，目标大小是(64, 64)
convert_png_to_ico('logo.png', 'output.ico', (64, 64))