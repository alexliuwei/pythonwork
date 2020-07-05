import json

'''获取文件内的姓名信息'''
file_pash = 'username.json'
def get_user_name():
    try:
        with open(file_pash) as file_object:
            username = json.load(file_object)
    except FileNotFoundError:
        print("《" + file_pash + "》" + "的文件未找到")
    else:
            return username


'''这是获取存储用户名信息的函数'''
def save_user_name():
    while True:
        name = input("请输入你的姓名，如需退出请输入Q")
        if name.lower() == 'q':
            break
        else:
            with open(file_pash,'w') as file1_object:
                json.dump(name,file1_object)
                print("用户" + name + "已保存")
                return name#把值返回给函数，后面好调取使用
                break


def greet_user():
     user_name = get_user_name()
     if user_name:
         print('欢迎回来' + user_name )
     else:
        save_user_name()



mese = '你的用户信息是否是：'

while True:
    name = get_user_name()
    try:
        qdname = input(mese + '"' + name+ '"' + " Y/N\n" )
    except KeyboardInterrupt:
        print("没有输入的退出\n")
        break
    else:
            if qdname.lower() == 'y':
                greet_user()
                break
            else:
                save_user_name()
                break