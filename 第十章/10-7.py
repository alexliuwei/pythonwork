'''这是10-7的练习题主要练习try except pass 在出错后让程序继续运行'''
while True:
    number1 = input("number1 please enber")
    number2 = input("number2 please enber")
    try:
        sum = int(number2) + int(number2)
    except :
        pass#出错后通过
    else:
        print(sum)

