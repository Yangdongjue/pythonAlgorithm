import sys

def reverse(x):
    output=0
    n=[]
    m=1
    while x//m!=0:
        p=x%(m*10)//m
        m*=10
        n.append(p)
    n.reverse()
    m=1
    for i in n:
        output+=(i*m)
        m*=10
    return output
        
    
def isPrime(x):
    for i in range(2,x+1):
        if i==x:
            return True
        elif x%i==0:
            return False

N= int(input())
M= list(map(int, input().split()))
k=[]
for i in M:
    if isPrime(reverse(i)):
        k.append(reverse(i))
for i in range(len(k)):
    if i!=len(k)-1:
        print(k[i], end=' ')
    elif i==len(k)-1:
        print(k[i])