# Demo2:
# 查找列表中元素，移除每个元素的空格，并查找以a或A开头且以c结尾的所有元素

li = ["alec", " aric", "Alex", "Tony", "rain"]
tu = ("alex", " aric", "Alec", "Tony", "rain")
dic = {'k1': "alec", 'k2': ' aric', "k3": "Alex", "k4": "Tony"}

new_li = []
new_tu = ()
new_dic = {}
for l in li:
    l = l.strip(' ')

    if l.startswith('a') or (l.startswith('A') and l.endswith('c')):
        new_li.append(l)
print(new_li)

for t in tu:
    t = t.strip(' ')
    #capitalize():把字母不分大小写匹配
    if t.capitalize().startswith('A') and t.endswith('c'):
        new_tu = list(new_tu)
        new_tu.append(t)
print(new_tu)

for key in dic:
    dic[key] = dic[key].strip(' ')
    if (dic[key].startswith('a') or dic[key].startswith('A')) and dic[key].endswith('c'):
        new_dic[key]=dic[key]
print(new_dic)
