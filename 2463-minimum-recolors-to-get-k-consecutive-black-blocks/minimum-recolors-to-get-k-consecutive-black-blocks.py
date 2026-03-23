class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:
        n = len(blocks)
        curr = blocks[:k].count("W")
        min_ = curr
        for i in range(k,n):
            if blocks[i-k] == "W":
                curr -=1
            if blocks[i]== "W":
                curr +=1
            min_ = min(min_,curr)
        return min_
