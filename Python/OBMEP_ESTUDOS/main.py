X = [1,1]

for i in range(1,101):
    X[0] = i
    for l in range(1,101):
        X[1] = l
        total = (X[0]+X[1])**2 -(X[0]**2 +X[1]**2)
        if total == 36:
            print(X)