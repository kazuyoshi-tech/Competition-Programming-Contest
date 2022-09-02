from typing import List, Optional
from collections import defaultdict, deque

# from collections import Counter
# from collections import defaultdict
# from bisect import bisect_right
# from copy import copy
# from collections import deque


class Solution:
    def maxSumTwoNoOverlap(self, nums: List[int], firstLen: int, secondLen: int) -> int:
        fir, sec = [], []
        len_nums = len(nums)
        tmp_f = 0
        for i in range(len_nums):
            tmp_f += nums[i]
            if firstLen <= i:
                tmp_f -= nums[i - firstLen]
            if firstLen - 1 <= i:
                fir.append([tmp_f, i - firstLen + 1, i])
        tmp_s = 0
        for i in range(len_nums):
            tmp_s += nums[i]
            if secondLen <= i:
                tmp_s -= nums[i - secondLen]
            if secondLen - 1 <= i:
                sec.append([tmp_s, i - secondLen + 1, i])
        sec = sorted(sec, key=lambda x: -x[0])
        ans = -1
        for f_n, f_f, f_g in fir:
            for s_n, s_f, s_g in sec:
                if s_g < f_f or f_g < s_f:
                    ans = max(ans, f_n + s_n)
                    break
        return ans


S = Solution()
nums = [2, 1, 5, 6, 0, 9, 5, 0, 3, 8]
firstLen = 4
secondLen = 3
print(S.maxSumTwoNoOverlap(nums, firstLen, secondLen))
