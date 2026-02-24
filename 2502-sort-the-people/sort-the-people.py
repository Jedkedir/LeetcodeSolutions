class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        #Using Bubble Sort
        n = len(names)
        for i in range(n):
            swap = False
            for j in range(0, n-i-1):
                if heights[j] < heights[j+1]:
                    heights[j], heights[j+1] = heights[j+1], heights[j]
                    names[j], names[j+1] = names[j+1], names[j]
                    swap = True
            if (swap == False):
                break
        return names