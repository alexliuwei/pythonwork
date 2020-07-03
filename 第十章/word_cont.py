def word_cont(file_name):
    try:
        with open(file_name) as file_object:
            file = file_object.read()
    except FileNotFoundError :
        print("没有找到名字为" + "《" + file_name + "》"+ "的文件")
    except UnicodeDecodeError :
        print("编码格式不是UTF-8")
    else:
        words = file.split()
        sum = len(words)
        print("《" + file_name + "》" + "有"  +  str(sum) + "个字" )

file_name = ['62535-0.txt','62540-8.txt','62543-8.txt','那些苦不堪言的日子']

for i in file_name:
    word_cont(i)
