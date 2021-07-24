def Perfect():
    a = int(input("Enter a number: "))
    sum = 0
    for x in range(1,a):
        if(a % x == 0):
            sum += x
    if(sum == a):
        print("The number is perfect")
    else:
        print("The number is imperfect")
    menu()


def Armstrong():
    a = int(input("Enter a number: "))
    b = len(str(a))
    sum = 0
    c = a
    while (a > 0):
        r = a % 10
        sum += r ** b
        a //= 10
    if(sum == c):
        print("The number is Armstrong")
    else:
        print("The number is not Armstrong")
    menu()


def Palindrome():
    a = input("Enter a number: ")
    b = a[::-1]
    print(b)
    if (a == b):
        print("The number is palindrome")
    else:
        print("The number is not palindrome")
    menu()



def menu():
    s = input("Enter the option\n1:Perfect Numbern\n2:Armstrong Number\n3:Palindrome\n4:Exit\n")
    if s == '1':
        Perfect()
    elif s == '2':
        Armstrong()
    elif s == '3':
        Palindrome()
    elif s == '4':
        exit()
    else:
        print("Something went wrong")
menu()
