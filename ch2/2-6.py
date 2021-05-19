import sys
def digit_sum(x):
    n=1
    sum=0
    while True:
        if x//n==0:
            n/=10
            break
        else: n*=10
    
    while True:
        k=x//n
        x=x-k*n
        sum+=k
        if(n==1):
            break
        else: n/=10
    return sum
    
N= int(input())
arr=list(map(int, input().split()))
sumArr=[]
for i in arr:
    sum=digit_sum(i)
    sumArr.append(sum)
max=0
for i in range(len(sumArr)):
    if max<sumArr[i]:
        max=sumArr[i]

output = sumArr.index(max)
print(arr[output])
