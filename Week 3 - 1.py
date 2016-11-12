def Reverse(String):
    String = String.split(' ')
    n = len(String)
    x = []
    while n > 0:
        x.append(String[n-1])
        n = n-1
    return(' '.join(x))

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
        
        
def noVowel(String, x):
    #x must be 0
    vowles = ["a", "e", "i", "o", "u"]
    String = String.replace(vowles[x],"")
    print(String)
    if x < 4:
        noVowel(String, x+1)
        


