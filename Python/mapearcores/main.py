def mapear(x):
    in_min = 0
    in_max = 255

    out_min = 0
    out_max = 1
    return float((x - in_min) * (out_max - out_min) / (in_max - in_min) + out_min)


x = float(input())
print(mapear(x,))