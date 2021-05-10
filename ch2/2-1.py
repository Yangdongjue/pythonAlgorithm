import sys
#sys.stdin=open("input.txt", "rt")

i=1
count=0
number, inputCount = map(int, input().split())

while True:
    if number%i==0:
        count+=1
    if count==inputCount:
        print(i);
        break
    if i==number and count<inputCount:
        print(-1)
        break
    i+=1

#정답 코드
'''
import sys
sys.stdin=open("input.txt","rt")
n, k = map(int, input().split)
cnt=0
for i in range(1, n+1):
    if n%i==0:
        cnt+=1
    if cnt==k:
        print(i)
        break
else:
    print(-1)
'''