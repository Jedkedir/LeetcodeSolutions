class Solution:
    def diffWaysToCompute(self, expression: str) -> List[int]:
        memo = {}
        def helper(x):
            if x in memo:
                return memo[x]
            res = []
            for i, ch in enumerate(x):
                if ch in "+-*":
                    l_res = helper(x[:i])
                    r_res = helper(x[i+1:])
                    for l in l_res:
                        for r in r_res:
                            if ch == '+':
                                res.append(l + r)
                            elif ch == '-':
                                res.append(l - r)
                            elif ch == '*':
                                res.append(l * r)
            if not res:
                res.append(int(x))
            memo[x] = res
            return res
        return helper(expression)