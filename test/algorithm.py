"""

算法题目链接
https://mp.weixin.qq.com/s/wYzUf4cx301etfPi7FrEwg
输入: heightMap = [[1,4,3,1,3,2],[3,2,1,3,2,4],[2,3,3,2,3,1]]
输出: 4
解释: 下雨后，雨水将会被上图蓝色的方块中。总的接雨水量为1+2+1=4。

输入: heightMap = [[3,3,3,3,3],[3,2,2,2,3],[3,2,1,2,3],[3,2,2,2,3],[3,3,3,3,3]]
输出: 10

下面是原题的解法：
def trapRainWater(self, heightMap: List[List[int]]) -> int:
    pq = []
    m = len(heightMap)  # 矩阵的高
    n = len(heightMap[0])  # 矩阵的宽
    visited = [[False for _ in range(n)] for _ in range(m)]

    # 先把四周所有元素添加到堆中。
    for i in range(m):
        for j in range(n):
            if i == 0 or i == m - 1 or j == 0 or j == n - 1:
                heapq.heappush(pq, (heightMap[i][j], i, j))
                visited[i][j] = True

    water = 0  # 接的雨水量
    # 上下左右
    dirs = [[0, -1], [0, 1], [-1, 0], [1, 0]]
    while pq:
        n0, n1, n2 = heapq.heappop(pq)
        for dx, dy in dirs:  # 遍历当前出队元素的上下左右四个方向。
            x = n1 + dx
            y = n2 + dy
            # 不能越界
            if x < 0 or x >= m or y < 0 or y >= n or visited[x][y]:
                continue
            visited[x][y] = True  # 标记为已计算过
            water += max(0, n0 - heightMap[x][y])  # 计算水量
            heapq.heappush(pq, (max(n0, heightMap[x][y]), x, y))
    return water

我这里提供了一个我个人的算法
"""
import heapq
from typing import List

height_map = [[1, 4, 3, 1, 3, 2], [3, 2, 1, 3, 2, 4], [2, 3, 3, 2, 3, 1]]

height_map2 = [[3, 3, 3, 3, 3], [3, 2, 2, 2, 3], [3, 2, 1, 2, 3], [3, 2, 2, 2, 3], [3, 3, 3, 3, 3]]


def trapRainWater(h_map):
    """
    :type h_map: List[List[int]]
    :rtype: int
    """
    if not h_map:
        return 0

    m, n = len(h_map), len(h_map[0])
    # print(m,n)
    rain = 0

    for i in range(1, m - 1):
        for j in range(1, n - 1):
            print("h[%d][%d]=%d" % (i, j, h_map[i][j]))
            # 先定义东南西北四个方向的边界最大值
            max_s = h_map[0][j]
            max_n = h_map[m - 1][j]
            max_e = h_map[i][0]
            max_w = h_map[i][n - 1]
            print("for i=", i, "j=", j, "max_s=", max_s, "max_n=", max_n, "max_e=", max_e, "max_w=", max_w)
            # 然后按照东南西北四个方向对某个元素对应的四个边界最大值进行判断，如果大于该最大值，则取新的最大值
            for k in range(0, i):
                if h_map[k][j] > max_s:
                    max_s = h_map[k][j]
            for k in range(i, m - 1):
                if h_map[k][j] > max_n:
                    max_n = h_map[k][j]
            for k in range(0, j):
                if h_map[i][k] > max_e:
                    max_e = h_map[i][k]
            for k in range(j, n - 1):
                if h_map[i][k] > max_w:
                    max_w = h_map[i][k]
            # 然后将东南西北四个方向的最大值再取最小值与这个元素的值相减，就是存储的雨水量，但要注意的是，如果该值小于0，说明不会储水，则取0
            rain += max(min(max_s, max_n, max_e, max_w) - h_map[i][j], 0)
            print("for i=", i, "j=", j, "max_s=", max_s, "max_n=", max_n, "max_e=", max_e, "max_w=", max_w)
            print(rain)
            return rain


# trapRainWater(height_map)
# trapRainWater(height_map2)


def trapRainWater2(heightMap: List[List[int]]) -> int:
    pq = []
    m = len(heightMap)  # 矩阵的高
    n = len(heightMap[0])  # 矩阵的宽
    visited = [[False for _ in range(n)] for _ in range(m)]

    # 先把四周所有元素添加到堆中。
    for i in range(m):
        for j in range(n):
            if i == 0 or i == m - 1 or j == 0 or j == n - 1:
                heapq.heappush(pq, (heightMap[i][j], i, j))
                visited[i][j] = True

    water = 0  # 接的雨水量
    # 上下左右
    dirs = [[0, -1], [0, 1], [-1, 0], [1, 0]]
    while pq:
        n0, n1, n2 = heapq.heappop(pq)
        for dx, dy in dirs:  # 遍历当前出队元素的上下左右四个方向。
            x = n1 + dx
            y = n2 + dy
            # 不能越界
            if x < 0 or x >= m or y < 0 or y >= n or visited[x][y]:
                continue
            visited[x][y] = True  # 标记为已计算过
            water += max(0, n0 - heightMap[x][y])  # 计算水量
            heapq.heappush(pq, (max(n0, heightMap[x][y]), x, y))
    return water


print(trapRainWater2(height_map2))
