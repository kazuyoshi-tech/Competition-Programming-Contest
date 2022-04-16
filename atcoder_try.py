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

INF = float("inf")
MOD1 = 10**9 + 7
MOD2 = 998244353

from math import gcd
from collections import defaultdict

N, K = map(int, input().split())
XY = [list(map(int, input().split())) for _ in range(N)]
if K == 1:
    print("Infinity")
    exit()

ans = set()
for i in range(N):
    x1, y1 = XY[i]
    memo = defaultdict(int)
    memo_p = defaultdict(list)
    for j in range(N):
        if i == j:
            continue
        x2, y2 = XY[j]
        dx, dy = (x2 - x1), (y2 - y1)
        g = gcd(dx, dy)
        dx, dy = dx // g, dy // g
        memo[(dx, dy)] += 1
        memo[(-dx, -dy)] += 1
        memo_p[(dx, dy)].append(j)
        memo_p[(-dx, -dy)].append(j)
    for key in memo.keys():
        ddx, ddy = key
        if K <= memo[key] + 1:
            ans.add((ddx, ddy, tuple(memo_p[key])))
print(len(ans) // 4)
