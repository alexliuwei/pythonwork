'''
pizz = "请输入你要选择的配料:"
message = ''

while message != 'quit':
    message =  input(pizz)
    print("我们会在您的披萨中添加" + message)


agem = '请输入你的年龄查看你的票价'
agem += "\n输入 quit 退出程序"

Active = True
while Active == True :
    age = input(agem)
    if age == 'quit':
        break
    elif int(age) <= 0:
        print("输入的年龄不合法，程序自动退出")
        Active = False
    else:
        age = int(age)
        if age < 3 :
            print("你的票价免费")
        elif age > 3 and age <= 12:
            print("你的票价5元")
        else:
            print("您的票价10元")


user = ['alex','eric','toto']
enduser = []

while user:
    userinfo = user.pop()
    enduser.append(userinfo)

for i in enduser:
    print(i)


user = ['alex','eric','toto','bobo','alex','jojo','alex']

while 'alex' in user:
     continue
print(user)
'''

respones = {}

po_active = True

while po_active :
    name = input("你的姓名")
    dif = input("你喜欢的地方")
    respones[name] = dif
    jx = input("是否还有人要填写 ,yes/no")
    if jx == 'no':
        po_active = False
print(respones)