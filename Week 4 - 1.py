def Binary(OrderedList, bottom, top):
    # Bottom and Top: User defined range
    while bottom != top+1:
        # ^ Generates the number to be searched
        print(bottom)
        number = bottom
        lower = 0
        upper = len(OrderedList)
        # Lower and Upper: Calculated search area reset each search
        result = False
        while (result == False) and (lower <= upper):
            middle = (lower+upper)//2
            if OrderedList[middle] == number:
                result = True
                # Break loop if search is the middle number
            else:
                if number < OrderedList[middle]:
                    upper = middle-1
                    #Create new range from start to one before middle
                else:
                    lower = middle+1
                    #Create new range from end to one above middle
        # ^ Binary searches for the current number
        if result == True:
            return True
        # ^ If at any point True, return true
        else:
            if bottom == top:
                return False
            # ^ If the range is completed without True
            else:
                bottom += 1
            # ^ Range not complete, true not found
