with open('day2.txt') as f:
    lines = f.readlines()

    distance = 0
    depth = 0

    for line in lines:
        if "forward" in line:
            distance = distance + int(line[8:])
        if "down" in line:
            depth = depth + int(line[5:])
        if "up" in line:
            depth = depth - int(line[3:])


print (distance)
print (depth)