class Solution:
    def validSequence(self, word1: str, word2: str) -> list[int]:
        n, m = len(word1), len(word2)
        if m > n:
            return []

        last0 = [-1] * (m + 1)
        last0[m] = n
        p = n - 1
        for k in range(m - 1, -1, -1):
            while p >= 0 and word1[p] != word2[k]:
                p -= 1
            if p < 0:
                break
            last0[k] = p
            p -= 1

        pos = defaultdict(list)
        for idx, ch in enumerate(word1):
            pos[ch].append(idx)

        last1 = [-1] * (m + 1)
        last1[m] = n
        for k in range(m - 1, -1, -1):
            opt1 = last0[k + 1] - 1 if last0[k + 1] > 0 else -1
            lst = pos[word2[k]]
            idx_in_lst = bisect_left(lst, last1[k + 1]) - 1
            opt2 = lst[idx_in_lst] if idx_in_lst >= 0 else -1
            last1[k] = max(opt1, opt2)

        ans = []
        w1_idx = 0
        changed = False

        for i in range(m):
            found = False
            while w1_idx < n:
                j = w1_idx
                match = (word1[j] == word2[i])
                if match:
                    need = last0[i + 1] if changed else last1[i + 1]
                    valid = (i == m - 1 or need > j)
                else:
                    if changed:
                        valid = False
                    else:
                        valid = (i == m - 1 or last0[i + 1] > j)

                if valid:
                    ans.append(j)
                    if not match:
                        changed = True
                    w1_idx = j + 1
                    found = True
                    break
                w1_idx += 1

            if not found:
                return []

        return ans