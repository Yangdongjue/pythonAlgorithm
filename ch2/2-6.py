import sys

N= int(input())
arr=list(map(int, input().split()))
sumArr=[]
for i in arr:
    n=1
    sum=0
    while True:
        if i//n==0:
            n/=10
            break
        else: n*=10
    
    while True:
        k=i//n
        i=i-k*n
        sum+=k
        if(n==1):
            break
        else: n/=10
    sumArr.append(sum)
max=0
for i in range(len(sumArr)):
    if max<sumArr[i]:
        max=sumArr[i]

output = sumArr.index(max)
print(arr[output])
