import re

with open("input7.txt") as f:
    currentDir, sizePerDir = "root", {}
    changeDir, isFile = re.compile("\$ cd ([.{2}|a-zA-Z]+)"), re.compile("(\d+) *\.*")

    def parent_dir(my_dir):
        return my_dir[:my_dir.rindex('/')]

    for line in f.readlines():
        if changeDir.search(line):
            newDir = re.findall(changeDir, line)[0]
            if newDir == "..":
                currentDir = parent_dir(currentDir)
            elif newDir != "/":
                currentDir += "/" + newDir

        if isFile.search(line):
            size = int(re.findall(isFile, line)[0])
            path = currentDir
            while True:
                sizePerDir[path] = sizePerDir.get(path, 0) + size
                if path == "root":
                    break
                path = parent_dir(path)

    space = 70000000 - max(sizePerDir.values())

    print("first puzzle answer = " + str(sum(filter(lambda size: size <= 100000, sizePerDir.values()))))
    print("second puzzle answer = " + str(min(filter(lambda size: space + size >= 30000000, sizePerDir.values()))))
