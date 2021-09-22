"""
Python program to find the largest element and its location.
"""

def largest_element(a,loc):
    """ Return the largest element of a sequence a.
    """

    maxval = a[0]
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

if __name__ == "__main__":

    a = [1,2,3,2,1]
    print("Largest element is {:}".format(largest_element(a)))
