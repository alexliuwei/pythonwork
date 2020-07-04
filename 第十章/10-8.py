file_name = 'dogs.txt'

try:
    with open(file_name,'r') as file_objiect:
        file = file_objiect.read()
except FileNotFoundError:
        print("《" + file_name + "》" + "文件不存在" )
else:
        print(file)

