try:
    while True:
        first_number  = input('first_number')
        if first_number.lower() == 'q':
            break
        second_number = input( 'second_number')
        if second_number.lower() == 'q':
            break
        anas = int(first_number)  / int(second_number)
        print(anas)
except ZeroDivisionError:
    print("不能处理0的数字")
