class Solution:
    def findRestaurant(self, list1: List[str], list2: List[str]) -> List[str]:
        lookup = {restaurant: i for i, restaurant in enumerate(list1)}
        res = []
        min_sum = float('inf')
        for j, restaurant in enumerate(list2):
            if restaurant in lookup:
                i = lookup[restaurant]
                current_sum = i + j
                if current_sum < min_sum:
                    min_sum = current_sum
                    res = [restaurant]
                elif current_sum == min_sum:
                    res.append(restaurant)
        return res