def log(*msg):
    b = []
    for index, a in enumerate(msg):
        b.append(str(msg[index]))
    with open("log", "a") as f:
        f.writelines(b)
        f.writelines("\n") 
