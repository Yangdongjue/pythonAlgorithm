import sys
#sys.stdin=open("input.txt", "rt")

N=int(input())
lst=list(map(int,input().split()))
lst2=[]
sum=0

for i in lst:
    sum=sum+i
sum=int(round(sum/N,0))

for i in range(0,N):
    if lst[i]-sum>0:
        tmpt=lst[i]-sum
    else:
        tmpt=sum-lst[i]
    lst2.append(tmpt)

min=0

for i in range(0,N):    
    if lst2[min]>lst2[i]:
        min=i
    elif lst2[min]==lst2[i]:
        if lst[min]>=lst[i]: min=min
        elif lst[min]<lst[i]: min=i
    else:
        continue
    
print("{} {}".format(sum, min+1))