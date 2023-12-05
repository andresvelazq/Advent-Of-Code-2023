values = []
sum = 0
spell = ["zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
digit = ['z0o', 'o1e', 't2o', 't3e', 'f4r', 'f5e', 's6x', 's7n', 'e8t', 'n9e']

file = open("Inputs/day1.txt", "r")

for line in file:
    for spelling in spell:
        if spelling in line:
            line = line.replace(spelling, digit[spell.index(spelling)])

    start = 0
    end = len(line) - 1

    while not line[start].isdigit():
        start += 1
    while not line[end].isdigit():
        end -= 1

    result = line[start] + line[end]    
    sum += int(result)

print(sum)
file.close()

