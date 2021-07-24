# without function

a = int(input())
f=1
if a<0 :
    print("The factorial does not exists for negative numbers")
elif a==0:
    print("The factorial of zero is 1")
else:
    for i in range(1,a+1):
        f=f*i
    print("The factorial of",a,"is",f)

# with Function
def fac(a):
    f=1
    if a<0 :
        print("The factorial does not exists for negative numbers")
    elif a==0:
        print("The factorial of zero is 1")
    else:
        for i in range(1,a+1):
            f=f*i
        print("The factorial of",a,"is",f)

b = int(input())
fac(b)