from typing import List, Optional
from collections import defaultdict, deque

# from collections import Counter
# from collections import defaultdict
# from bisect import bisect_right
# from copy import copy
# from collections import deque


class Solution:
    def minKBitFlips(self, nums: List[int], k: int) -> int:
        len_nums = len(nums)
        memo = [0] * len_nums
        cnt = 0
        ans = 0
        for i in range(len_nums - k + 1):
            cnt += memo[i]
            if (nums[i] + cnt) % 2 == 0:
                memo[i] += 1
                if i + k < len_nums:
                    memo[i + k] -= 1
                cnt += 1
                ans += 1
        for i in range(len_nums - k + 1, len_nums):
            cnt += memo[i]
            if (nums[i] + cnt) % 2 == 0:
                return -1
        return ans


nums = [0, 0, 0, 1, 0, 1, 1, 0]
k = 3
S = Solution()
print(S.minKBitFlips(nums, k))
