'''
정점의 개수 N과 간선의 개수 M
둘째 줄부터 M개의 줄에 간선의 양 끝 점 u와 v가 주어짐
인접 행렬과 인접 리스트 출력

Input
6 5
1 2
2 5
5 1
3 4
4 6

Output
[[0, 0, 0, 0, 0, 0, 0],
 [0, 0, 1, 0, 0, 1, 0],
 [0, 1, 0, 0, 0, 1, 0],
 [0, 0, 0, 0, 1, 0, 0],
 [0, 0, 0, 1, 0, 0, 1],
 [0, 1, 1, 0, 0, 0, 0],
 [0, 0, 0, 0, 1, 0, 0]]
[[], [2, 5], [1, 5], [4], [3, 6], [2, 1], [4]]
'''
import pprint
n, m = map(int, input().split())
matrix = [[0] * (n + 1) for i in range(n + 1
)]
list_ = [[] for i in range(n + 1)]
for i in range(m):
    x, y = map(int, input().split())
    # 인접 행렬
    matrix[x][y] = 1
    matrix[y][x] = 1

    # 인접 리스트
    list_[x].append(y)
    list_[y].append(x)

pprint.pprint(matrix)
print(list_)