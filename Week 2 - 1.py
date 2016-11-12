def Perfect(x):
    total = 1
    counter = 1
    while x > total:
        total = counter * counter
        counter = counter + 1
    if total > x:
        counter = counter - 2
        total = counter * counter
    return total

