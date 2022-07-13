def binarySearch(arr, x):
    left = 0
    right = len(arr)-1
    
    while (left <= right):
        mid = (left + right)//2
        if (arr[mid] == x):
            return mid
        elif (x < arr[mid]):
            right = mid-1
        else:
            left = mid+1
    
    return -1

def solution(arr, s):
	# buoc 1
    temp = []
    temp.append(arr[0])
    for i in range(1, len(arr)):
        temp.append(temp[i-1] + arr[i])

	# buoc 2
    for k in range(0, len(temp)):
        if (temp[k] > s):
            break
    l = binarySearch(arr, temp[k]-s)
    if (l == -1):
        return -1
    else:
        for j in range(l+1, k+1):
            print(arr[j])
    

if __name__ == "__main__":
    arr = list(map(int, input().split()))
    s = int(input())
    solution(arr, s)