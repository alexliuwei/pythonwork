file_name = 'guest.txt'
name = input("请输入你的姓名：")


with open(file_name,'w') as file_object:
    file = file_object.write(name)
