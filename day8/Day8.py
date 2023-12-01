input8 = open("input8.txt", "r").read().split("\n")
forrest, width, height = "".join(input8), len(input8[0]), len(input8) - 1
rows = map(lambda row: map(int, list(row)), input8)
columns = map(lambda col: map(lambda row: int(forrest[row * width + col: row * width + col + 1]), range(height)), range(width))
treeIndex, visible, treeScores = 0, 0, []

def tree_size(index):
    return int(forrest[index: index + 1])

def on_edge_of_grid(row, column):
    return row in [0, (len(rows) - 1)] or column in [0, (column == width - 1)]

def is_visible_from(trees):
    return all(t < tree_size(treeIndex) for t in trees)

def count(trees):
    tree_count = 0
    for tree in trees:
        tree_count += 1
        if tree >= tree_size(treeIndex):
            return tree_count
    return tree_count


while treeIndex < len(forrest):
    rowNr, columnNr = treeIndex / width, treeIndex % width

    left = rows[rowNr][:columnNr]
    right = rows[rowNr][columnNr + 1:]
    above = columns[columnNr][:rowNr]
    below = columns[columnNr][rowNr + 1:]

    treeScores.append(count(reversed(left)) * count(right) * count(reversed(above)) * count(below))

    if on_edge_of_grid(rowNr, columnNr) or is_visible_from(left) or is_visible_from(right) or is_visible_from(above) or is_visible_from(below):
        visible += 1
    treeIndex += 1

print("first puzzle answer = " + str(visible))
print("second puzzle answer = " + str(max(treeScores)))
