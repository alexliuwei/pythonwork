'''这是10-10的练习题主要练习把文件读出来后怎么处理本次练使用。count（）方法看文本中有多少个括号内的字'''
file_name = '62535-0.txt'

with open(file_name,'r') as file_object:
    file = file_object.read()
    lin  = file.lower().count('the')#查看文件中有多少个'the'的单词
    print(lin)