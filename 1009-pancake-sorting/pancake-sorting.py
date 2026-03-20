class Solution:
    def pancakeSort(self, arr: List[int]) -> List[int]:
        def flip(right):
            left = 0
            while left < right:
                arr[left],arr[right]=arr[right],arr[left]
                right-=1
                left+=1
        n = len(arr)
        res = []
        for i in range(n-1,-1,-1):
            max_ = i
            for j in range(i,-1,-1):
                if arr[j]>arr[max_]: 
                    max_ = j
            if max_!= i:
                flip(max_)
                flip(i)
                res.append(max_+1)
                res.append(i+1)
        return res