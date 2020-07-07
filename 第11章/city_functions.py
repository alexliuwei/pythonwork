'''这是11-1和11-2的练习题用于接受城市名称的函数'''
"""

def get_ciy_name(city,country):#定义一个城市名称的函数有2个形参
    city_name = city + ',' + country
    return city_name.title()#把值返回给函数，用title()的方法把每个单词的第一个字母转换为大写
"""
'''11-2'''
def get_ciy_name(city,country,population=''):#定义一个城市名称的函数有3个形参其中最好一个是可选用默认值空代替
    if population:
        city_name = city + ',' + country +' ' + 'population' + ' ' + str(population)
    else:
        city_name = city + ',' + country
    return city_name.title()
