def larger(a,loc=False):
    try:
        maxval = a[0]
        indicii = 0
        for i in range(1, len(a)):
            if a[i] > maxval:
                maxval = a[i]
                indicii = i

        large = sorted(a)
        index = len(a)
        if loc == True:
    #return large[index-1]
            return maxval,indicii
        else:
            return maxval

    except ValueError:
        print("ah gee rick")
    except TypeError:
        print("Type Error son")

b = ['a',5,'d',2,8,'z']
larger(b)