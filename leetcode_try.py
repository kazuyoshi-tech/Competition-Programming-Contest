from typing import List

# from collections import Counter
# from collections import defaultdict
# from bisect import bisect_right
# from copy import copy
# from collections import deque


class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        from collections import defaultdict

        nums_memo = defaultdict(int)
        nums_memo[0] = 1
        ans = 0
        tmp = 0
        for num in nums:
            tmp = (tmp + num) % k
            ans += nums_memo[tmp]
            nums_memo[tmp] += 1
        return ans


nums = [5]
k = 9
S = Solution()
print(S.subarraysDivByK(nums, k))
