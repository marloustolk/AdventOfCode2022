with open("input6.txt") as f:
    codes, seen, marker = [], [], 1

    for code in f.readlines():
        for char in code:
            codes.append(char)
            if len(codes) == 5:
                codes.pop(0)
            if len(codes) == 4 and not any(i in seen or seen.append(i) for i in codes):
                break
            marker += 1
            seen = []

    print("first puzzle answer = " + str(marker))

with open("input6.txt") as f:
    codes, seen, marker = [], [], 1

    for code in f.readlines():
        for char in code:
            codes.append(char)
            if len(codes) == 15:
                codes.pop(0)
            if len(codes) == 14 and not any(i in seen or seen.append(i) for i in codes):
                break
            marker += 1
            seen = []

    print("second puzzle answer = " + str(marker))