with open('text.txt' , 'r') as f:
    for line in f:
        temp = line.split(' ')
        if 'error' in temp:
            print(line)