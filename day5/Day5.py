with open("input5.txt") as f:
    stackNr, crates, cratesNewCrane = 1, [], []

    for line in f.readlines():
        if line.find("[") >= 0:
            while stackNr < len(line):
                index = (stackNr - 1) / 4
                if index > (len(crates) - 1):
                    crates.append([])
                    cratesNewCrane.append([])
                if line[stackNr].isalpha():
                    crates[index].append(line[stackNr])
                    cratesNewCrane[index].append(line[stackNr])
                stackNr += 4
            stackNr = 1
        if line.find('move') >= 0:
            count, fromStack, toStack = line.replace("move ", "").replace("from", "to").split(" to ")
            for i in range(int(count)):
                crate = crates[int(fromStack) - 1].pop(0)
                crates[int(toStack) - 1].insert(0, crate)

                crateNewCrane = cratesNewCrane[int(fromStack) - 1].pop(0)
                cratesNewCrane[int(toStack) - 1].insert(i, crateNewCrane)

    answer1, answer2 = "", ""
    for column in crates:
        answer1 += column[0]
    for column in cratesNewCrane:
        answer2 += column[0]
    print("first puzzle answer = " + answer1)
    print("second puzzle answer = " + answer2)
