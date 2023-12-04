values = []
sum = 0

file = open("Day-1/input.txt", "r")

for line in file:
    line = line.strip("\n")
    start = 0
    end = len(line) - 1
    while not line[start].isdigit():
        start += 1
    while not line[end].isdigit():
        end -= 1
    result = line[start] + line[end]    
    values.append(result)

for value in values:
    sum += int(value)

print(sum)


