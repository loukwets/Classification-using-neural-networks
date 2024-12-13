def readData(filename):
    f = open(filename)
    L = []
    for line in f:
        elem = [ int(s) for s in line.strip().split(',') ]
        L += [ elem ]
    return L
