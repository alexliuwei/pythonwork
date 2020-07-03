'''这是读取和写入文件的课后题'''
file_ptch = 'learning_python'#定义一个变量为文件名

with open(file_ptch) as file_object:#用with 让python 自动完成文件的关闭，用OPEN方法打开一个文件并把内容传给file_object
    python = file_object.readlines()#用readlines()把文件写入一个字典中


for i in python:
    i = i.replace('alex','crys')#替换字符
    i = i.replace('python','C')
    print(i.strip())

filename = 'mytext.txt'
with open(filename,'w') as file1_object:#第二个实惨为模式。'r','w','a','r+' 分别代表读、写、追加、读写、模式
    mytxt = file1_object.write(str(12312344) + '\n')
    mytxt = file1_object.write('I Love python !\n')

with open(filename,'a') as file3_object:#追加写入模式
    mytxt1 = file3_object.write('I love c# \n')
    mytxt1 = file3_object.write('I love .net core \n')
    print(mytxt1)
print(mytxt1)
print(mytxt)


