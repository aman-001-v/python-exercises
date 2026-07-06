with open('text.txt.txt','r') as f1:
    with open('text_c.txt' , 'w') as f2:
        for line in f1:
            f2.write(line)