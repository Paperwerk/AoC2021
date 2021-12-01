with open('day1.txt') as f:
    lines = f.readlines()
    total = 0
    new_list = []
    for count, item in enumerate(lines):
        try:
            new_list.append(sum((int(lines[count]), int(lines[count+1]), int(lines[count+2]))))
        except IndexError:
            pass

    for count, item in enumerate(new_list):
        if count > 0:
            if item > new_list[count-1]:
                total = total + 1

    print(total)