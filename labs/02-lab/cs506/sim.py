import math

def euclidean_dist(x, y):
    res = 0
    for i in range(len(x)):
        res += (x[i] - y[i])**2
    return res**(1/2)

def manhattan_dist(x, y):
    #raise NotImplementedError()
    s = 0
    for i in range(len(x)):
        s += abs(x[i] - y[i])
    return s

def jaccard_dist(x, y):
    #raise NotImplementedError()
    intersect = len(list(set(x))).intersection(y)
    union = (len(x) + len(y)) - intersect
    return float(intersect)/union

def cosine_sim(x, y):
    #raise NotImplementedError()
    sumxx, sumxy, sumyy = 0, 0, 0
    for i in range(len(x)):
        temp1 = x[i]
        temp2 = y[i]
        sumxx +=temp1*temp1
        sumyy += temp2*temp2
        sumxy += temp1*temp2
    return sumxy/math.sqrt(sumxx*sumyy)

def minkowski_dist(x, y, p):
    s = 0
    for i in range(len(x)):
        s += abs(x[i] = y[i])**p
    return res**(1/p)


    

# Feel free to add more
