#coding: utf-8
import cmd
# 存放敏感词文件的路径
filtered_words_filepath = '/Users/mren-ext/Documents/filtered_words.txt'
class CLI(cmd.Cmd):

    def __init__(self): #初始基础类方法
        cmd.Cmd.__init__(self)  # 初始化，提取敏感词列表
        self.intro = 'Python敏感词检测:' #输出欢迎信息
        f = open(filtered_words_filepath)
        self.words = list(map(lambda i: i.strip('\n'), f.readlines()))
        print(self.words)
        self.prompt = ">>> "    # 定义提示符

    def default(self, line):
        if any([i in line for i in self.words]):
            print ('****')
        else:
            print (line)

    def do_quit(self, arg):
        exit()
        return True

if __name__ =="__main__":
    cli = CLI()
    cli.cmdloop()

# print(any([0,1]))
# print(all([0,1]))