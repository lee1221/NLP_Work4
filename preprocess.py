import re
import os

filePath = r"./datasets/"  # 文件夹路径
fileList = os.listdir(filePath)
pchinese = re.compile('([\u4e00-\u9fa5]+)+?')  # 判断是否为中文的正则表达式
fw1 = open('./processed/zhwiki.txt', 'w')


for file in fileList:
    f = open(os.path.join(filePath, file))
    print(file)
    for line in f.readlines():
        for x in line:
            if len(x.encode('utf-8')) == 3 and x != '　':
                fw1.write(x)
            if x in ['\n'] and line != '\n':  # 以部分中文符号为分割换行
                fw1.write('\n')

    f.close()

fw1.close()


