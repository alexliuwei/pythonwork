while True:
    number1 = input("请输入第一个数字按q退出")
    if number1.lower() == 'q':
        break
    number2 = input("请输入第二个数字按q退出")
    if number2.lower() == 'q':
        break
    try:
        sum = int(number1) +int(number2)
    except ValueError:
        print("不是数字")
    else:
        print(sum)