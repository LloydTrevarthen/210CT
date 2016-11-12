def Randomise(array):
    from random import randint
    x = len(array)
    permlength = x
    y = []
    z = []
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
# Rationale behind this shuffle:
# Using the randint function, the while loop iterates once for every int within the array
# generating a number between 0 and the length of the array-1. This number is then checked
# to see if it is in the hidden list y, which holds a record of which numbers have been selected
# from the array. If it isn't present, the number is added to y, and the array[num] is added to z,
# the output list. This ensures the function still shuffles EG [1,1,1,2] as each positon is shuffled
# rather than each number, where duplicates would be issues.
# Finally the z ouput array is check to see if it matches the starting array, if so the function
# recurs until a shuffled output is achieved.


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


    
    
# Advanced task
def Alien(eggs, days, hatchrate):
    alientotal = 1
    eggtable = []
    for a in range(hatchrate):
        days = days - 1
        eggtable.append(alientotal*eggs)
        # Sets up the table with the first "eggs", where no multiplication occours
        
    while days > 0:
        days = days - 1
        alientotal = alientotal + eggtable[0]
        eggtable.pop(0)
        eggtable.append(alientotal*eggs)
        # Adds the total on from the front of the queue, and appends the new egg total
        # to the rear. FIFO queue the length of hatchrate.
    print(alientotal)
    
# Treats the hatchrate as an "incubation time" or buffer within eggtable, before the number is added to
# the rest of the system.
        
    
    
