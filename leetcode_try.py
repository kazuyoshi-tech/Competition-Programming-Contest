from typing import List

# from collections import Counter
# from collections import defaultdict
# from bisect import bisect_right
# from copy import copy
# from collections import deque


class Solution:
    def powerfulIntegers(self, x: int, y: int, bound: int) -> List[int]:
        from bisect import bisect_right

        x_pow, y_pow = [1], [1]
        ans = set()
        while x_pow[-1] <= bound and x != 1:
            x_pow.append(x_pow[-1] * x)
        while y_pow[-1] <= bound and y != 1:
            y_pow.append(y_pow[-1] * y)
        for x_base in x_pow:
            if bound <= x_base:
                break
            tar = bound - x_base
            i_b = bisect_right(y_pow, tar)
            for i in range(i_b):
                ans.add(x_base + y_pow[i])
        return sorted(list(ans))


x = 2
y = 1
bound = 10
S = Solution()
print(S.powerfulIntegers(x, y, bound))
