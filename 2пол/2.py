for x in range(2):
    for y in range(2):
        for w in range(2):
            for z in range(2):
                if (not(y<=x) or (z<=w) or not(z))==0:
                    print(x,y,w,z)
