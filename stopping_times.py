def stopping_time(z: int):
    s=[]
    s.append(z)
    while z>1:
        if z%2==0:
            n=z//2
            s.append(n)
            z=n
        else:
            n=3*z+1
            s.append(n)
            z = n
    return len(s)-1

