file_name = 'guest_book.txt'

ac = True

mes = '请输入你的姓名:\n'
mes += '按Q结束程序'
while ac == True:
     with open(file_name,'a') as file_object:
         name = input(mes)
         if name.lower() != 'q':
            print("欢迎您" + name)
            name = file_object.write(name+"\n")
         else:
             ac = False