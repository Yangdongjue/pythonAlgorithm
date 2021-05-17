arr = [5,3,7,9,2,5,2,6]
arrMin=float('inf') #무한대로 초기화
for i in range(len(arr)):
    if arr[i]<arrMin:
        arrMin=arr[i]
print(arrMin)
