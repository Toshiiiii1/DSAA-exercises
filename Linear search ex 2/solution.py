def solution(arr):
    minValue = min(arr)
    maxValue = max(arr)
    
	# tim gia tri nho nhat dau tien
    for i in range(0, len(arr)):
        if (arr[i] == minValue):
            break
	# tim gia tri lon nhat cuoi cung
    for j in range(len(arr)-1, -1, -1):
        if (arr[j] == maxValue):
            break
        
    temp = arr[i]
    arr[i] = arr[j]
    arr[j] = temp
    
    print(arr)


if __name__ == "__main__":
    arr = list(map(int, input().split()))
    solution(arr)