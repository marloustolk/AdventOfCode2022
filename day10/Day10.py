instructions = open("input10.txt", "r").read().split("\n")
cycle, X, signal_strength_sum = 0, 1, 0
cycle_signal_checks = [20, 60, 100, 140, 180, 220]
crt_drawing, sprite_positions = "", [0, 1, 2]

for instruction in instructions:
    cycles_in_instruction = 1 if instruction == "noop" else 2
    for cycle_nr in range(cycles_in_instruction):
        cycle += 1
        crt_drawing += "#" if (cycle - 1) % 40 in sprite_positions else "."
        crt_drawing += "\n" if cycle % 40 == 0 else ""
        if cycle in cycle_signal_checks:
            signal_strength_sum += cycle * X
        if cycle_nr == 1:
            addx = int(instruction.split(" ")[1])
            X += addx
            sprite_positions = [pos + addx for pos in sprite_positions]

print(crt_drawing)
print("first puzzle answer = " + str(signal_strength_sum))
print("second puzzle answer = ECZUZALR")