def interpolationSearch(arr, x):
    l, r = 0, len(arr)-1
    while (x >= arr[l] and x <= arr[r] and l <= r):
        probe = l + (r-l) * (x-arr[l]) // (arr[r]-arr[l])
        if (arr[probe] == x):
            return probe
        elif (arr[probe < x]):
            l = probe+1
        else:
            r = probe-1
            
    return -1

if __name__ == "__main__":
    arr = list(map(int, input().split()))
    x = int(input())
    print(interpolationSearch(arr, x))