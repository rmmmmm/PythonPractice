# Demo5:
# list的简便生成，列表生成式
list1 = [i * i for i in range(1, 5)]
print(list1)
# [1, 4, 9, 16]

list2 = [m + n for m in 'abc' for n in 'def']
print(list2)
# ['ad', 'ae', 'af', 'bd', 'be', 'bf', 'cd', 'ce', 'cf']

d = {'a': '1', 'b': '2', 'c': '3'}
list3 = [k + '=' + v for k, v in d.items()]
print(list3)


# ['a=1', 'b=2', 'c=3']

# 斐波那契数列
def fib(num):
    n, a, b = 0, 0, 1
    while n < num:
        print(b)
        a, b = b, a + b
        n += 1
    # def一个函数，如果没有return的话就会自动返回输出一个'None'
    return 'done'


print(fib(5))

