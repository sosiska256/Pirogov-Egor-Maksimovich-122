for a in range(100):
    for x in range(10000):
        if all(x%3!=0 =< x%5!=0) or (x+a)>=70:
            print(a)
