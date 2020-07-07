'''这是employee的类测试'''
import unittest
from employee import Employee

class Test_employee(unittest.TestCase):#切记要继承unittest.TestCase的父类

    def setUp(self) -> None:#用setUp创建一个对象给测试的方法使用，好处是可以在整个类使用，应为是存储在变量self中
        self.def_info = Employee('alex','liu',2000)

    def test_give_def_rais(self):
        self.def_info.give_raise()#调用上面setUp那个变量
        self.assertEqual(self.def_info.annualsaalary,7000)

    def test_user_rais(self):
        self.def_info.give_raise(1000)
        self.assertEqual(self.def_info.annualsaalary,3000)

if __name__ == '__main__':
    unittest.main()

