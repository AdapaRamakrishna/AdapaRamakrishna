n=int(input())
d=n
w=n
l=0
while n:
    l+=1
    n=n//10
s=0    
while d:
    r=d%10
    s+=r**l
    d=d//10
if s==w:
    print('Armstrong')
else:
    print('Not an Armstrong')

