n = int(input("enter the number"))
def fib(n):
    if(n==0):
        return 0
    elif(n==1):
        return 1
    elif(n==2):
        return 1
    elif(n==3):
        return 2
    else:
        return fib(n-1) + fib(n-2)

