n=int(input("enter a  number"))
l=1
while n:
    r=n%10
    n=n//10
    l*=n
print(l)
