# Demo1:
# 有如下集合 [11,22,33,44,55,66,77,88,99,90],将所有大于66的值保存在字典的第一个key中，小余的保存在第二个key中
# 即：{'k1':大于66，'k2'：小于66}

list1 = [11, 22, 33, 44, 55, 66, 77, 88, 99, 90]
doc = {'alt':[],
       'glt':[]}
for l in list1:
    if l>66:
        doc['alt'].append(l)
    elif l<66:
        doc['glt'].append(l)
    else:
        pass
print(doc)