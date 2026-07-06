with open ('text.txt.txt' , 'r') as f:
    l = 0
    c = 0
    w = 0
    f_contents = f.read()
    for i in f_contents:
        c += 1
        if i == ' ':
            w += 1
        elif i == '\n':
            l += 1
            w += 1
    print(l + 1 , " " , c , " " , w)