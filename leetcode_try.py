from typing import List, Optional
from collections import defaultdict, deque

# from collections import Counter
# from collections import defaultdict
# from bisect import bisect_right
# from copy import copy
# from collections import deque


class Solution:
    def numSquarefulPerms(self, nums: List[int]) -> int:
        self.ans = 0
        nums.sort()

        def dfs(tmp_nums, nums):
            if len(nums) == 0:
                self.ans += 1
                return
            for i in range(len(nums)):
                if 0 < i and nums[i] == nums[i - 1]:
                    continue
                if len(tmp_nums) == 0 or (
                    0 < len(tmp_nums)
                    and int((nums[i] + tmp_nums[-1]) ** 0.5) ** 2
                    == nums[i] + tmp_nums[-1]
                ):
                    dfs(tmp_nums + [nums[i]], nums[:i] + nums[i + 1 :])

        dfs([], nums)
        return self.ans


nums = [2, 2, 2]
S = Solution()
print(S.numSquarefulPerms(nums))
