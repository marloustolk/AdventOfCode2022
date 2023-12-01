with open("input9.txt") as f:
    caloriesList = []
    elfCalories = 0

    for line in f.readlines():
        if line == "\n":
            caloriesList.append(elfCalories)
            elfCalories = 0
        else:
            elfCalories += int(line)
    caloriesList.append(elfCalories)

    highestCalories = []
    for i in [0, 1, 2]:
        maxCalories = max(caloriesList)
        highestCalories.append(maxCalories)
        caloriesList.remove(maxCalories)

    print("first puzzle answer =" + str(highestCalories[0]))
    print("second puzzle answer =" + str(sum(highestCalories)))
