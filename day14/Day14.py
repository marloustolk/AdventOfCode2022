rock_paths = open("input14.txt", "r").read().split("\n")
rocks, source, sand_units = set(), (500, 0), 0
first_puzzle_answer, is_blocked = 0, False

def get_point(string_point):
    [x, y] = string_point.split(",")
    return int(x), int(y)

def get_x(point):
    return point[0]

def get_y(point):
    return point[1]

def get_range(a, b):
    nrs = []
    [biggest, smallest] = sorted([a, b], reverse=True)
    for diff in range(biggest - smallest + 1):
        nrs.append(smallest + diff)
    return nrs

def fall_down(x, y):
    if cave[x][y + 1] not in ["#", "O"]:
        return x, y + 1
    if cave[x - 1][y + 1] not in ["#", "O"]:
        return x - 1, y + 1
    if cave[x + 1][y + 1] not in ["#", "O"]:
        return x + 1, y + 1
    return x, y

for path in rock_paths:
    points = path.split(" -> ")
    for point in range(len(points) - 1):
        a_x, a_y = get_point(points[point])
        b_x, b_y = get_point(points[point + 1])
        if a_x == b_x:
            for rock in get_range(a_y, b_y):
                rocks.add((a_x, rock))
        else:
            for rock in get_range(a_x, b_x):
                rocks.add((rock, a_y))

floor_height = max(map(get_y, rocks)) + 2

for floor in range(min(map(get_x, rocks)) - 200, max(map(get_x, rocks)) + 200):
    rocks.add((floor, floor_height))

y_coords = map(get_y, rocks)
x_coords = map(get_x, rocks)
cave = [["." for h in range(0, max(y_coords) + 1)] for w in range(0, max(x_coords) + 1)]

for x,y in rocks:
    cave[x][y] = "#"

while is_blocked == False:
    x, y = source
    if fall_down(x, y) == source:
        is_blocked = True
    while (x, y) != fall_down(x, y):
        x, y = fall_down(x, y)
    if y == (max(y_coords) - 1) and first_puzzle_answer == 0:
        first_puzzle_answer = sand_units
    sand_units += 1
    cave[x][y] = "O"

drawing = ""
for y in range(0, len(cave[0])):
    if y < 10:
        drawing += "00" + str(y)
    elif y < 100:
        drawing += "0" + str(y)
    else:
        drawing += str(y)
    for x in range(0, len(cave)):
        if (x, y) == source:
            drawing += "+"
        elif x > 400:
            drawing += cave[x][y]
    drawing += "\n"
print drawing

print("first puzzle answer = " + str(first_puzzle_answer))
print("second puzzle answer = " + str(sand_units))
