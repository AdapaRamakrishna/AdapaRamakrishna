#use of functions
print("pick 1 opt to find the given number is even or odd")
print("pick 2 opt to find all the even numbers in a given range")
print("pick 3 opt to find all the odd numbers in a given range")
opt=int(input("enter the number"))
if opt==1:
    n=int(input("enter the number"))
    if n%2==0:
        print("even")
    else:
        print("odd")
elif opt==2:
    a,b=map(int,input("enter two numbers").split())
    for i in range(a,b+1):
        if i%2==0:
            print(i,end=" ")
else:
    a,b=map(int,input("enter two numbers").split())
    for i in range(a,b+1):
        if i%2!=0:
            print(i,end=" ")

