'''
age = 22

if age <= 0 :
    print("inter wrong")
elif age >= 18:
    print("You are old enough to vote")
    print("have you regustered to vote yet?")
else:
    print("sorry ,you are too young to vote.")
    print("please register to vote as soon as you turn 18!")
'''

age = 2

if age < 4:
    price = 0
elif age <= 18:
    price = 5
else:
    price = 20

print("you cost is $" +str(price)+" .")