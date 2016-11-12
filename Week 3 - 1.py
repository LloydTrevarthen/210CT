def Reverse(String):
    String = String.split(' ')
    n = len(String)
    x = []
    while n > 0:
        x.append(String[n-1])
        n = n-1
    return(' '.join(x))
# Splits string between spaces, returns each word into a list back to front, joins and prints.

def isPrime(x, y):
    #y must be 2
    if x == 1:
        return("Prime")
    if x == 2:
        return("Prime")
    else:
        if x % y == 0:
            if x == y:
                print("Prime")
            else:
                print("Not Prime")
        else:
            return(isPrime(x, y+1))
# If x == 1, or == 2, return prime, beyond this perform the following:
# Check if x is evenly divisible by 2. If it is, return Not Prime, if it isn't
# Reccur through again with the divider being y+1, so 3, 4, 5...
# If x == y without a even divisible being found, the number is prime.
        
        
def noVowel(String, x):
    #x must be 0
    vowles = ["a", "e", "i", "o", "u"]
    String = String.replace(vowles[x],"")
    if x < 4:
        noVowel(String, x+1)
    if x == 4:
        print(String)
# Itterate through the vowles list from 0 to 4, replacing any matches in
# the defined string with a blank entry. Return string once complete.
        


