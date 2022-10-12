from typing import List, Optional

# from collections import Counter
# from collections import defaultdict
# from bisect import bisect_right
# from copy import copy
# from collections import deque

# MOD = 10**9 + 7


class Solution:
    def numEquivDominoPairs(self, dominoes: List[List[int]]) -> int:
        from collections import defaultdict

        memo = defaultdict(int)
        ans = 0
        for a, b in dominoes:
            if b < a:
                a, b = b, a
            ans += memo[(a, b)]
            memo[(a, b)] += 1
        return ans


S = Solution()
dominoes = [[1, 2], [1, 2], [1, 1], [1, 2], [2, 2]]
print(S.numEquivDominoPairs(dominoes))
