class Solution:
    def finalValueAfterOperations(self, operations: List[str]) -> int:
        ops = {
            "--X":-1,
            "++X":1,
            "X--":-1,
            "X++":1
        }
        x = 0
        for op in operations:
            val = ops.get(op,0)
            if val > 0:
                x += 1
            elif val < 0:
                x -= 1
            else:
                pass
        return x