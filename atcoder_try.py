# from collections import Counter
# import re
# import copy
# import itertools
# from sys import stdin
# from collections import deque
# from copy import copy
# from itertools import combinations
# from bisect import bisect
# import heapq
# import sys
# from collections import defaultdict
# memo = defaultdict(int)

import sys

sys.stdin.readline
sys.setrecursionlimit(10**7)
MOD = 10**9 + 7
INF = float("inf")

N, A = map(int, input().split())
X = list(map(int, input().split()))
dp = [[0] * (50 * N + 1) for _ in range(N + 1)]
dp[0][0] = 1
for x in X:
    for i in range(N + 1, 0, -1):
        for j in range(50 * N + 1):
            if 0 <= j - x and dp[i - 1][j - x] != 0:
                dp[i][j] += dp[i - 1][j - x]
ans = 0
for i in range(1, N + 1):
    ans += dp[i][i * A]
print(ans)
