with open("input4.txt") as f:
    overlappingAsignments = 0
    overlappingSections = 0

    for line in f.readlines():
        elf1, elf2 = line.split(",")
        sectionsElf1 = range(int(elf1.split("-")[0]), int(elf1.split("-")[1]) + 1)
        sectionsElf2 = range(int(elf2.split("-")[0]), int(elf2.split("-")[1]) + 1)
        if all(elem in sectionsElf1 for elem in sectionsElf2) or all(elem in sectionsElf2 for elem in sectionsElf1):
            overlappingAsignments += 1
        if any(section in sectionsElf1 for section in sectionsElf2) or any(section in sectionsElf2 for section in sectionsElf1):
            overlappingSections += 1

    print("first puzzle answer = " + str(overlappingAsignments))
    print("second puzzle answer = " + str(overlappingSections))
