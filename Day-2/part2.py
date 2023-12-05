sum = 0
power = []

file = open("Day-2/input.txt", "r")

def get_mins(pull, minrgb):
    match pull[1]:
        case "red":
            if int(pull[0]) > minrgb[0]:
                minrgb[0] = int(pull[0])
        case "green":
            if int(pull[0]) > minrgb[1]:
                minrgb[1] = int(pull[0])
        case "blue":
            if int(pull[0]) > minrgb[2]:
                minrgb[2] = int(pull[0])
    return minrgb

for line in file:
    minrgb = [0,0,0]

    line = line.strip("\n")
    games = line.split(": ")
    sets = games[1].split("; ")
    for set in sets:
        pulls = set.split(", ")
        for pull in pulls:
            pull = pull.split(" ")
            minrgb = get_mins(pull, minrgb)
    power.append(minrgb[0] * minrgb[1] * minrgb[2])

for value in power:
    sum += value

print(sum)
    
