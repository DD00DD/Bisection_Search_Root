
def find_root3(x, epsilon):
    '''
    Assume: x, epsilon are floating point numbers and epsilon > 0
    Use bisection search to find the following root of x such that
    If x >=0, return y such that x - epsilon <= y ** 4 <= x + epsilon
    Else, return y such that x - epsilon <= y ** 3 <= x + epsilon

    Note: You must use bisection search to implement the function.
    '''
    high = max(1,x)
    low = 0
    y = (high + low)/2

    while abs(y**3 - x) >= epsilon and abs(y**4 - x) >= epsilon:
        if y**3 < x and y**4 < x:
            low = y
        else:
            high = y
        y = (high + low)/2
        print(y)

        if x >= 0:
            if x - epsilon <= y**4 <= x + epsilon:
                return y
        else:
            if x - epsilon <= y**3 <= x + epsilon:
                return y
    
