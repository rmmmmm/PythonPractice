# test与test1是使用__name__ == '__main__'与否的对比
# 随机生成10个20位的激活码（网上答案）
import random
import string
FIELD = string.digits + string.ascii_letters
def generate(n, many=1, where=None):
    def getCode(n):
        return "".join(random.sample(FIELD, n))
    gene = [getCode(n) for i in range(many)]
    return gene
def writeIn(n, many, where):
    count = 1
    for i in generate(n, many):
        with open(where, "a") as boom:
            boom.write(str(count).rjust(3)+"  "+i+"\n")
        count += 1

# __name__ == '__main__'：只有在运行本模块时才会调用，如果是其他模块导入本模块的话，就不会执行函数下的内容
if __name__ == '__main__':
    writeIn(20, 200, "coupon.txt")

# 如果不使用__name__ == '__main__'直接调用函数的话，在本模块或其他模块导入的情况下都会执行
# writeIn(20, 200, "coupon.txt")

