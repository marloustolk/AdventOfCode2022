with open("input2.txt") as f:
    rock, paper, scissors = 1, 2, 3
    draw, win = 3, 6
    value = {'A': rock, 'B': paper, 'C': scissors, 'X': rock, 'Y': paper, 'Z': scissors}
    score = 0
    for line in f.readlines():
        opponent = value[line[0]]
        me = value[line[2]]
        if opponent == rock and me == scissors or opponent == paper and me == rock or opponent == scissors and me == paper:
            score += me
        elif opponent == me:
            score += draw + me
        else:
            score += win + me
    print("first puzzle answer = " + str(score))

with open("input2.txt") as f:
    rock, paper, scissors = 1, 2, 3
    lose, draw, win = 0, 3, 6
    value = {'A': rock, 'B': paper, 'C': scissors, 'X': lose, 'Y': draw, 'Z': win}
    score = 0
    for line in f.readlines():
        opponent = value[line[0]]
        needTo = value[line[2]]
        if opponent == rock and needTo == lose:
            score += scissors
        elif opponent == rock and needTo == win:
            score += win + paper
        elif opponent == paper and needTo == lose:
            score += rock
        elif opponent == paper and needTo == win:
            score += win + scissors
        elif opponent == scissors and needTo == lose:
            score += paper
        elif opponent == scissors and needTo == win:
            score += win + rock
        else:
            score += draw + opponent
    print("second puzzle answer = " + str(score))
