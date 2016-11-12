def Randomise(array):
    from random import randint
    x = len(array)
    permlength = x
    y = []
    z = []
    global z
    while x > 0:
        num = randint(0,(permlength-1))
        if num not in y:
            x = x - 1
            y.append(num)
            z.append(array[num])
    if array != z:
        print(z)
    else:
        print("Randomised array = starting array...",z)
        Randomise(array)



def Trailing(number):
    #from math import factorial
    #number = factorial(number)
    #x = -1
    #while number == int(number):
        #number = number/10
        #x = x + 1
    #print(x)
    #Doesn't work as Python rounds numbers above 16 digits

    division = 1
    power = 1
    total = 0
    while division >= 1:
        division = number/(5**power)
        total = total+(int(division))
        power = power + 1
        # Never works out the factorial.
        # Divides the x! by 5^1 then 5^2...
        # Adds the results together, to get trailing zeros
        # Stops when the divison is >= 1
    print(total)


def Alien(eggs, days, hatchrate):
    alientotal = 1
    eggtable = []
    for a in range(hatchrate):
        days = days - 1
        eggtable.append(alientotal*eggs)
    while days > 0:
        days = days - 1
        alientotal = alientotal + eggtable[0]
        eggtable.pop(0)
        eggtable.append(alientotal*eggs)
    print(alientotal)
        
        
    
    
