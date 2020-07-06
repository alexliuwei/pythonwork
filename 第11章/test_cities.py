'''这是11-1的练习题'''
'''这是个单元测试，定义了一个方法用于测试get_ciy_name这个函数的正确性'''
import unittest#导入单元测试
from  city_functions import get_ciy_name#导入自己编写的模块文件中的get_ciy_name函数

class City_test(unittest.TestCase):#定义了一个类继承unittest.TestCase
    def test_city_name(self):#定义了一个方法
        city_name = get_ciy_name('cq','china')#调用get_ciy_name函数给实参并把值赋值给变量
        self.assertEqual(city_name,'Cq,China')#用assertEqual方法比对输出的结果是否一直


if __name__ == '__main__':#如果程序在本文件用运行就运行if语句以下的代码，如果是已模块的方式导入就不运行if以下的代码相当于一个程序的虚拟入口
    unittest.main()
