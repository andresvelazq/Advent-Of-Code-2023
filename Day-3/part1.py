sum = 0
schematic = []

#file = open("Day-3/example.txt", "r")
file = open("Inputs/day3.txt", "r")

for line in file:
    line = line.strip("\n")
    schematic.append(list(line))
file.close()

def symbol_search(left, right, above, current, below, test):
    '''Search surrounding cells for symbols'''
    if left < 0:
        left = 0

    search = [above[left:right+1], current[left:right+1], below[left:right+1]]

    for row in search:
        for cell in row:
            if cell == '.' or cell.isdigit():
                continue
            else:
                return True
    return False

current = []
for row in range(len(schematic)):
    #establish current and surrounding rows
    above = current
    current = schematic[row]

    if row + 1 >= len(schematic):
        below = []
    else:
        below = schematic[row + 1]
    
    numFound = False
    curr_num = 0
    for column in range(len(current)):
        if not numFound and not current[column].isdigit():
            continue
        elif not current[column].isdigit() or column == len(current) - 1:
            if current[column].isdigit():
                curr_num = int(curr_num) * 10
                curr_num += int(current[column])
            if symbol_search(left, column, above, current, below, row):
                sum += int(curr_num)
            curr_num = 0
            numFound = False
            continue

            
        if not numFound:
            left = column - 1
            curr_num = current[column]
            numFound = True
            continue

        curr_num = int(curr_num) * 10
        curr_num += int(current[column])

print(sum)
        