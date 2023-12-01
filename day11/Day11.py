class Monkey:
    def __init__(self, items, operation, test, throw_to):
        self.items = items
        self.operation = operation
        self.test = test
        self.throw_to = throw_to
        self.inspected_items = 0


monkey_notes = open("input11.txt", "r").read().split("\n\n")

def read_monkey_notes():
    monkeys = []
    for monkey in monkey_notes:
        monkey_note = monkey.split("\n")
        items = [int(num) for num in monkey_note[1].split(": ")[1].split(", ")]
        operation = monkey_note[2].split("old ")[1].split(" ")
        test = int(monkey_note[3].split("by ")[1])
        throw_to = [int(note.split("monkey ")[1]) for note in [monkey_note[4], monkey_note[5]]]
        monkeys.append(Monkey(items, operation, test, throw_to))
    return monkeys

monkeys = read_monkey_notes()
for round in range(20):
    for monkey in monkeys:
        for item in monkey.items:
            times = item if monkey.operation[1] == "old" else int(monkey.operation[1])
            worry_level = (item * times if monkey.operation[0] == "*" else item + times) / 3
            other_monkey = 1 if worry_level % monkey.test else 0
            monkeys[monkey.throw_to[other_monkey]].items.append(worry_level)
            monkey.inspected_items += 1
        monkey.items = []
inspected_items = sorted(map(lambda monkey: monkey.inspected_items, monkeys), reverse=True)
print("first puzzle answer = " + str(inspected_items[0] * inspected_items[1]))


stress_reducer = reduce((lambda x, y: x * y), map(lambda monkey: monkey.test, monkeys))

monkeys = read_monkey_notes()
for round in range(10000):
    for monkey in monkeys:
        for item in monkey.items:
            times = item if monkey.operation[1] == "old" else int(monkey.operation[1])
            worry_level = (item * times if monkey.operation[0] == "*" else item + times)
            other_monkey = 1 if worry_level % monkey.test else 0
            worry_level = worry_level % stress_reducer
            monkeys[monkey.throw_to[other_monkey]].items.append(worry_level)
            monkey.inspected_items += 1
        monkey.items = []

inspected_items = sorted(map(lambda monkey: monkey.inspected_items, monkeys), reverse=True)
print("second puzzle answer = " + str(inspected_items[0] * inspected_items[1]))
