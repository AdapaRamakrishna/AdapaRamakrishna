def is_prime(n):
    if n==1:
        return false
    for i in range(2,n//2+1):
        if n%i==0:
            return False
        return True
def primes_in_range(a,b):
    for i in range(a,b+1):
        if is_prime(i):
            print(i,end=" ")
def composites_in_range(a,b):
    for i in range(a,b+1):
        if not is_prime(i):
            print(i,end=" ")             
a,b=map(int,input().split())
composites_in_range(a,b)
