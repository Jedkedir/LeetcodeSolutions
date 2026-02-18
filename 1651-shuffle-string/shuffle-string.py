class Solution:
    def restoreString(self, s: str, indices: List[int]) -> str:
        n = len(indices)
        my_dict = dict(map(lambda x,y:(x,s[y]),indices,range(n)))
        res = []
        for i in range(n):
            res.append(my_dict[i]) 
        return ''.join(res)