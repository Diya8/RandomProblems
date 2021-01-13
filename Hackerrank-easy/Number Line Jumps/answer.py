def kangaroo(x1, v1, x2, v2):
    if x1<x2 and v1<v2:
        return "NO"
    elif x2<x1 and v2<v1:
        return "NO"
    else:
        if v1 == v2: #div by zero
            return "NO"
        if (x1-x2)%(v1-v2) == 0: # x1 + y*v1 should be equal to x2 + y*v2 where y is the no. of jumps made
            return "YES"
        else:
            return "NO"
