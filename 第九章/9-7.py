'''9-5'''
class User():
    def __init__(self,user_name,user_age):
        self.user_name = user_name
        self.user_age = user_age
        self.login_attempts = 0

    def increment_login_attempts(self):#定义一个方法让属性累加
        self.login_attempts += 1

    def reset_attemptss(self):#定义一个方法让属性归0
        self.login_attempts = 0

    def get_user_login_attempts_print(self):
        print("该用户登录的次数为第" + str (self.login_attempts) + "次")

    def get_user_login_attempts(self):
        print(self.login_attempts)


user = User('a',12)


for i in range(1,51):#用for 循环让累加的方法执行50次
    user.increment_login_attempts()
    user.get_user_login_attempts_print()


Active = True

while Active == True:#用while循环让用户自主选择是否要清除记录
    cl = input("该用户登录" + str(user.login_attempts) + "次，是否需要清除Y/N")
    if cl.lower() == 'y':#判断是否需要清除
      user.reset_attemptss()#调用类清除的方法
      user.get_user_login_attempts_print()
      break#清除后跳出循环
    else:
        cm = input("用户记录未清除，登录次数为" + str(user.login_attempts) + "次，是否继续清除Y/N" )
        if cm.lower() == 'y':
            continue#如果用户选择继续清除重新开始上面的while判断
        else:
            Active = False

user.get_user_login_attempts()

class Privileges():
    def __init__(self):
        self.privileges = ['can add post', 'can delete post', 'can ban user']
        self.userpri =  ['read','down','push']





class Admin(User):
    def __init__(self,user_name,user_age):
        super(Admin, self).__init__(user_name,user_age)
        self.privilege = Privileges()

    def show_privileges(self):
        for i in self.privilege.privileges:
            print(i)

    def show_userpri(self):
        for i in self.privilege.userpri:
            print(i)

admin = Admin('admin',31)
admin.show_privileges()
admin.get_user_login_attempts()
admin.increment_login_attempts()
admin.get_user_login_attempts()

