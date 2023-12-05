possible = []
red = 12
green = 13
blue = 14
sum = 0

file = open("Day-2/input.txt", "r")

def check_possible(counts):
    match counts[1]:
        case "red":
            if int(counts[0]) > red:
                return False
        case "green":
            if int(counts[0]) > green:
                return False
        case "blue":
            if int(counts[0]) > blue:
                return False
    return True


for line in file:
    impossible = False
    games = line.split(": ")
    game = games[0].strip("Game ")
    games[1] = games[1].strip("\n")
    sets = games[1].split("; ")
    for set in sets:
        pulls = set.split(", ")
        for pull in pulls:
            counts = pull.split(" ")
            if not check_possible(counts):
                impossible = True
                break
        if impossible:
            break
    if impossible:
        continue
    possible.append(game)
                    
for game in possible:
    sum += int(game)

print(sum)
            
