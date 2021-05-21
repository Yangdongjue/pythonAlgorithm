import sys

N= int(input())
m=[2]
for i in range(3, N+1):
    for j in m:
        if i%j==0:
            break;
        if  j==m[len(m)-1] and i%j!=0:
            m.append(i)
            break;

print(len(m))

cnt=0
#배열 선언
#k=[]
#for i in range(N+1):
#    k.append(0)
k=[0]*(N+1)

for i in range(2,N+1):
    if k[i]==0:
        cnt+=1
        for j in range(1,N//i+1): #for j in range(i, n+1, i):
            k[j*i]=1

print(cnt)