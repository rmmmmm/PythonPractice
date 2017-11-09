# demo7:随机生成10个20位的激活码，并写入code.txt中
import string
import random

# string.digits 是所有数字 string.ascii_letters是所有大小写字母
mystring = string.digits + string.ascii_letters

# "with open as"的mode默认为'r', 所以后面不设置可写模式的话，因为是初次建立此文件，所以会报错：找不到这个文件；
# 如果可写的话，会自动建立这个文件在里面写入东西，也就能找到这个文件了，也就不会报错了
with open("code.txt", 'w') as code:
    for i in range(10):
        # "".join 这个方法可以把list中的元素合在一起变为字符串
        # simple（字符串,数字）:在字符串中随意选取20个随机生成新的字符串
        code.write("".join(random.sample(mystring, 20)) + '\n')
