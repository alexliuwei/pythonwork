'''这是10-12的练习题，主要练习函数json.dump 和json.load'''
import json#导入json函数

mes = "请输入您喜欢的数字，按Q退出"
file_name = 'number.json'

try:
    with open(file_name, 'r') as file1_object:
        print_number = json.load(file1_object)#加载json的文件
except FileNotFoundError:
    while True:
        number = input(mes)
        if number.lower() == 'q':
            break
        with open(file_name, 'a') as file_object:
            save_nmber = json.dump(number, file_object)#写入json的文件
            print("你喜欢的数字是：" + number)
else:
    print("你喜欢的数字是：" + print_number)


