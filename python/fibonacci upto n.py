n=int(input("enter the number"))
a=0
b=1
s=0
c=a+b
while (c<=n):
    if c%2==0:
        s+=c
    a,b =b,c
    c=a+b
print(s)
   
