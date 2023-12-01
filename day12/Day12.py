import collections

map_rows = open("input12.txt", "r").read().split("\n")
heightmap, start, end, paths = {}, [], [], []
position = []


def find(grid, start):
    queue = collections.deque([[start]])
    seen = set([start])
    while queue:
        path = queue.popleft()
        x, y = path[-1]
        if grid[y][x] == goal:
            return path
        for x2, y2 in ((x+1,y), (x-1,y), (x,y+1), (x,y-1)):
            if 0 <= x2 < width and 0 <= y2 < height and grid[y2][x2] != wall and (x2, y2) not in seen:
                queue.append(path + [(x2, y2)])
                seen.add((x2, y2))

wall, clear, goal = "#", ".", "*"
width, height = 10, 5
grid = ["..........",
        "..*#...##.",
        "..##...#*.",
        ".....###..",
        "......*..."]
path = find(grid, (5, 2))
print path
# [(5, 2), (4, 2), (4, 3), (4, 4), (5, 4), (6, 4)]

# for row in range(len(map_rows)):
#     for col in range(len(map_rows[0])):
#         area = map_rows[row][col]
#         if area == "S":
#             start = (col, row)
#             heightmap[col, row] = "a"
#             position = (col, row)
#             paths.append([position[:]])
#         elif area == "E":
#             end = (col, row)
#             heightmap[col, row] = "z"
#         else:
#             heightmap[col, row] = area

print("first puzzle answer = " + str(0))
print("second puzzle answer = " + str(0))
