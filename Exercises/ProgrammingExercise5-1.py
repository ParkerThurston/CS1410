from collections import Counter

lyst = [3, 1, 7, 1, 4, 10]
length = len(lyst)

print("list:" +str(lyst))


def median(lyst):
    length = len(lyst)
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
        return median 
        

def mode(lyst):
    length = len(lyst)
    data = Counter(lyst)
    getMode = dict(data)
    mode = [k for k, v in getMode.items() if v == max(list(data.values()))]

    if len(mode) == length:
        mode = "0"
    else:
        return mode[0]

    


def mean(lyst):
    length = len(lyst)
    if not lyst:
        print(0)
    else:
        Lsum = sum(lyst)
        mean = Lsum / length
        return mean

modeS = mode(lyst)
medianS = median(lyst)
meanS = mean(lyst)
print("Mode: " + (str(modeS)))
print("Median: " + str(medianS))
print("Mean: "+ str(meanS))
