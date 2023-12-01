with open("input3.txt") as f:
    prioritySum = 0

    prioritySumElfGroups = 0
    elfGroup = []

    for line in f.readlines():
        firstCompartment, secondCompartement = line[:len(line) // 2], line[len(line) // 2:]
        found = False
        for item in firstCompartment:
            if not found and secondCompartement.find(item) >= 0:
                code = ord(item)
                prioritySum += code - 96 if item.islower() else code - 38
                found = True

        badgeFound = False
        if len(elfGroup) == 2:
            for item in line:
                if not badgeFound and elfGroup[0].find(item) >= 0 and elfGroup[1].find(item) >= 0:
                    code = ord(item)
                    prioritySumElfGroups += code - 96 if item.islower() else code - 38
                    badgeFound = True
                    elfGroup = []
        else:
            elfGroup.append(line)

    print("first puzzle answer = " + str(prioritySum))
    print("second puzzle answer = " + str(prioritySumElfGroups))