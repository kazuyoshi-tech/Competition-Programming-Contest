from typing import List, Optional
from functools import lru_cache

# from collections import Counter

# from collections import defaultdict
# from bisect import bisect_right
# from copy import copy
# from collections import deque

# MOD = 10**9 + 7


class Solution:
    def maximumSafenessFactor(self, grid: List[List[int]]) -> int:
        from collections import deque

        thif_diff = deque()
        H, W = len(grid), len(grid[0])
        diff_memo = [[-1] * W for _ in range(H)]
        for h in range(H):
            for w in range(W):
                if grid[h][w] == 1:
                    thif_diff.append([h, w, 0])
                    diff_memo[h][w] = 0
        while len(thif_diff):
            now_h, now_w, diff = thif_diff.popleft()
            for next_h, next_w in [
                [now_h + 1, now_w],
                [now_h - 1, now_w],
                [now_h, now_w + 1],
                [now_h, now_w - 1],
            ]:
                if (
                    0 <= next_h < H
                    and 0 <= next_w < W
                    and diff_memo[next_h][next_w] == -1
                ):
                    next_diff = diff + 1
                    diff_memo[next_h][next_w] = next_diff
                    thif_diff.append([next_h, next_w, next_diff])
        first_move = deque([[0, 0]])
        sec_move = deque()
        visited = [[-1] * W for _ in range(H)]
        visited[0][0] = diff_memo[0][0]
        while True:
            while len(first_move):
                now_h, now_w = first_move.popleft()
                for next_h, next_w in [
                    [now_h + 1, now_w],
                    [now_h - 1, now_w],
                    [now_h, now_w + 1],
                    [now_h, now_w - 1],
                ]:
                    if (
                        0 <= next_h < H
                        and 0 <= next_w < W
                        and visited[next_h][next_w] == -1
                    ):
                        if visited[now_h][now_w] <= diff_memo[next_h][next_w]:
                            visited[next_h][next_w] = visited[now_h][now_w]
                            first_move.append([next_h, next_w])
                        else:
                            sec_move.append([next_h, next_w, now_h, now_w])
            while len(sec_move):
                now_h, now_w, ex_h, ex_w = sec_move.popleft()
                visited[now_h][now_w] = visited[ex_h][ex_w]
                first_move.append([now_h, now_w])
            print(visited)
            if visited[-1][-1] != -1:
                return visited[-1][-1]


S = Solution()

grid = [[1, 1, 1], [1, 1, 1], [1, 0, 0]]  # 0
# grid = [[0, 1, 1], [0, 1, 1], [0, 0, 1]]
print(S.maximumSafenessFactor(grid))
