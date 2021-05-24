import sys

N=input()
M=[]
i=0
while True:
    if N[i]>='0' and N[i]<='9':
       M.append(int(N[i]))
    i+=1
    if i>len(N)-1:
        break
p=0
sum=0

for k in range(len(M)-1, -1,-1):
    if M[k]!=0:
        sum+=M[k]*(10**p)
    p+=1
q=1
count=0
while True:
    if sum%q==0:
        if sum==q**2:
            count+=1
        elif q>sum**(1/2):
            break
        else: count+=2
    q+=1
print(sum)
print(count)
