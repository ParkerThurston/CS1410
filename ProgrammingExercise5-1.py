from heapq import nlargest
from operator import itemgetter
lyst = [input("list:").split(",")]
length = len(lyst)

print("list:" +str(lyst))


def median(lyst,length):
    if not lyst:
        print(0)
    else:
        lyst.sort()
        if length % 2 == 0:
            median1 = lyst[length//2] 
            median2 = lyst[length//2 - 1] 
            median = (median1 + median2)/2
        else:
            median = lyst[length//2]
        print("Median: " + str(median))

#def mode(lyst,length):
    


def mean(lyst,length):
    if not lyst:
        print(0)
    else:
        Lsum = sum(lyst)
        mean = Lsum / length
        print("Mean: " + str(mean))

#mode(lyst,length)
median(lyst,length)
mean(lyst,length)
