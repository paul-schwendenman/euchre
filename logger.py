def log(*args, **kwargs):
    msg = []
    for item in args:
        msg.append(str(item))
    with open("log", "a") as f:
        if msg:
            f.writelines(msg)
            f.writelines("\n") 
        elif kwargs:
            f.writelines(str(kwargs))
            f.writelines("\n") 
        else:
            f.writelines("\n") 
                    