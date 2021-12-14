n=int(input("Enter a Number"))
t=n
b=n
l=0
while n:
    l+=1
    n=n//10
s=0
while t:
    r=t%10
    s+=r**l
    t=t//10
if s==b:
    print("The given number is an armstrong")
else:
    print("The given number is not an armstrong") 

    
    

    
    
            
            
