# demo6：图像处理，在图片上加个文字

# PIL:Python图像处理，需pip3 install pillow
# ImageFont字体，ImageDraw画图

# from PIL import Image, ImageDraw, ImageFont
# def add_num(img):
#     draw = ImageDraw.Draw(img)
#     # ImageFont.truetype()设置字体和大小，.ttf：包含TureType字体的OpenType文件后缀名为.ttf
#     myfont = ImageFont.truetype('Arial.ttf', size=140)
#     fillcolor = "#ff0000"
#     width, height = img.size
#     draw.text((width/2-70, height/2-70), '99', font=myfont, fill=fillcolor)
#     img.save('result.jpg','jpeg')
#     return 0
# if __name__ == '__main__':
#     image = Image.open('a.jpg')
#     add_num(image)
#     image.show()

from PIL import Image, ImageDraw, ImageFont

image = Image.open("a.jpg")
font = ImageFont.truetype('Arial.ttf', size=110)
draw = ImageDraw.Draw(image)
width, height = image.size
# 调用函数时，标准调用顺序不能换，关键字调用顺序可换
# 关键字调用：
draw.text(text='这是图片啊', font=font, fill='#00ff00', xy=(width / 2 - 70, height / 2 - 70))
# 标准调用：
# draw.text((width/2-70, height/2-70),'99', font, '#00ff00')
image.save("test.jpg")
