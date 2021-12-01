with open('day1.txt') as f:
    lines = f.readlines()
    total = 0
    for count, item in enumerate(lines):
        if count > 0:
            if item > lines[count-1]:
                total = total + 1

    print (total)