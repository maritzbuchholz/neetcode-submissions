class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        n = len(arr)
        for i in range(n-1):
            arr[i] = arr[i+1]
            for j in range(i+1,n):
                if arr[i] < arr[j]:
                    arr[i] = arr[j]
        arr[n-1] = -1
        return(arr)
        