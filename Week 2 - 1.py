# / Returns the highest perfect square of a number. /
def Perfect(x):
    total = 1
    counter = 1
    while x > total:
        total = counter * counter
        counter = counter + 1
        # Performs 1x1, 2x2, 3x3... until the answer is bigger than the input.
    if total > x:
        counter = counter - 2
        total = counter * counter
        # Corrects the overshoot of the previous calculation, outputting the correct answer.
        # -2 because of the +1 in the previous loop, and the additional -1 needed to undershoot.
    return total

