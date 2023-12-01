moves = open("input9.txt", "r").read().split("\n")
rope, diff_col, diff_row = {}, [], []
directions = {"R": [0, 1], "L": [0, -1], "U": [1, 0], "D": [-1, 0]}
visited_places = {}

for knot in range(10):
    rope[knot] = [0, 0]
    visited_places[knot] = []

for move in moves:
    [to, count] = move.split(' ')
    for nr in range(int(count)):
        directions_for_knot = directions[to]

        for knot in rope:
            if knot == 0:
                rope[knot][0] += directions_for_knot[0]
                rope[knot][1] += directions_for_knot[1]

                diff_col = rope[0][0] - directions[to][0]
                diff_row = rope[0][1] - directions[to][1]
            else:
                diff_col = rope[knot - 1][0] - rope[knot][0]
                diff_row = rope[knot - 1][1] - rope[knot][1]

                if abs(diff_col) > 1 or abs(diff_row) > 1:
                    if diff_col == 0:
                        rope[knot][1] += -1 if directions_for_knot[1] < 0 else 1
                    elif diff_row == 0:
                        rope[knot][0] += -1 if directions_for_knot[0] < 0 else 1
                    else:
                        diff_col = -1 if diff_col < 0 else 1
                        diff_row = -1 if diff_row < 0 else 1
                        rope[knot][0] += diff_col
                        rope[knot][1] += diff_row
                directions_for_knot = [diff_col, diff_row]
            visited_places[knot].append(rope[knot][:])

print("first puzzle answer = " + str(len(set(map(lambda pos: str(pos), visited_places[1])))))
print("second puzzle answer = " + str(len(set(map(lambda pos: str(pos), visited_places[9])))))
