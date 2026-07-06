with open('log.txt' , 'r') as f:
    n = 0
    e = 0
    i = 0
    w = 0
    u = 0
    for log in f:
        n += 1
        if 'ERROR' in log:
            e += 1
        elif 'WARNING' in log:
            w += 1
        elif 'INFO' in log:
            i += 1
        else:
            u += 1
    print(f"No. of line: {n}")
    print(f"INFO: {i}")
    print(f"WARNING: {w}")
    print(f"ERROR: {e}")
    print(f"UNKNOWN: {u}")