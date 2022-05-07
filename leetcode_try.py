from typing import List

# from collections import Counter
# from collections import defaultdict
# from bisect import bisect_right
# from copy import copy
# from collections import deque


class Solution:
    def numsSameConsecDiff(self, n: int, k: int) -> List[int]:
        nums = [str(i) for i in range(1, 10)]
        for _ in range(n - 1):
            tmp = []
            for num in nums:
                last = int(num[-1])
                if 0 <= last - k <= 9:
                    tmp.append(num + str(last - k))
                if k == 0:
                    continue
                if 0 <= last + k <= 9:
                    tmp.append(num + str(last + k))
            nums = tmp
        return nums


n = 3
k = 7
S = Solution()
print(S.numsSameConsecDiff(n, k))
