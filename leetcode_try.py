from typing import List, Optional
from functools import lru_cache

# from collections import Counter

# from collections import defaultdict
# from bisect import bisect_right
# from copy import copy
# from collections import deque

# MOD = 10**9 + 7


class Solution:
    def minimumTotalPrice(
        self, n: int, edges: List[List[int]], price: List[int], trips: List[List[int]]
    ) -> int:
        from collections import deque

        INF = float("inf")

        root = [[] for _ in range(n)]
        for s, g in edges:
            root[s].append(g)
            root[g].append(s)
        repeats = [0] * n
        for s, g in trips:
            step_cnt = [-1] * n
            step_cnt[s] = 0
            stack = deque([s])
            while len(stack):
                now = stack.popleft()
                for next in root[now]:
                    if step_cnt[next] == -1:
                        step_cnt[next] = step_cnt[now] + 1
                        stack.append(next)
            stack = deque([g])
            repeats[g] += 1
            while len(stack):
                now = stack.popleft()
                for next in root[now]:
                    if step_cnt[next] == step_cnt[now] - 1:
                        repeats[next] += 1
                        stack.append(next)

        @lru_cache(None)
        def dfs(vertex: int, parent: int, parent_halved: bool):
            # If parent already halved, then this vertex can't be halved, so give it a inf
            halved = INF if parent_halved else (price[vertex] * repeats[vertex]) // 2
            not_halved = price[vertex] * repeats[vertex]
            for next in root[vertex]:
                if next == parent:
                    continue
                if halved < INF:
                    halved += dfs(next, vertex, True)
                not_halved += dfs(next, vertex, False)
            return min(halved, not_halved)

        return dfs(0, -1, False)


S = Solution()

n = 4
edges = [[0, 1], [1, 2], [1, 3]]
price = [2, 2, 10, 6]
trips = [[0, 3], [2, 1], [2, 3]]
print(S.minimumTotalPrice(n, edges, price, trips))
