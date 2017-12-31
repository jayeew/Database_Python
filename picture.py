#!/usr/bin/python
# -*- coding: UTF-8 -*-

# 读入一张画，输出一个字符组成的字符画

# 需要用到的类库有：
# 1. pillow。可以使用pip install pillow
# http://pillow.readthedocs.io/en/latest/handbook/tutorial.html

# 灰度值 ＝ 0.2126 * r + 0.7152 * g + 0.0722 * b

from PIL import Image
import argparse

#命令行输入参数处理
parser = argparse.ArgumentParser()

# #输入文件
# parser.add_argument('DOGE.png')
# #输出文件
# parser.add_argument('-o', '--output')
# #输出字符画宽
# parser.add_argument('--width', type=int, default=160)
# #输出字符画高
# parser.add_argument('--height', type=int, default=60)
#
# #获取参数
# args = parser.parse_args()

IMG = '123.png'
WIDTH = 80
HEIGHT = 40
OUTPUT = 'output.txt'

ascii_char = list("@*`. ")


# 将256灰度映射到ascii_char个字符上
def get_char(r, b, g, alpha=256):
    if alpha == 0:
        return ' '
    length = len(ascii_char)
    gray = int(0.2126 * r + 0.7152 * g + 0.0722 * b)

    unit = (256.0 + 1)/length
    return ascii_char[int(gray/unit)]

# 在cmd 中直接运行.py文件,则__name__的值是'__main__';
# 而在import 一个.py文件后,__name__的值就不是'__main__'了;
# 从而用if __name__ == '__main__'来判断是否是在直接运行该.py文件
if __name__ == '__main__':

    im = Image.open(IMG)
    im = im.resize((WIDTH, HEIGHT), Image.NEAREST)

    txt = ""

    for i in range(HEIGHT):
        for j in range(WIDTH):
            txt += get_char(*im.getpixel((j, i)))
        txt += '\n'

    print txt

    #字符画输出到文件
    if OUTPUT:
        with open(OUTPUT, 'w') as f:
            f.write(txt)
    else:
        with open("output.txt", 'w') as f:
            f.write(txt)