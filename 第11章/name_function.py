'''用户吗标准转换函数'''

def get_name(first,list,middle=''):
    if middle:
        full_name = first + ' ' + middle  + ' ' + list
    else:
        full_name = first + ' ' + list
    return full_name.title()


