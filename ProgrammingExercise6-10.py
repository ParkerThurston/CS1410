


#def myRange(upper):
##    myList = []
#    lower = 0
#    while  lower < upper:   
#        myList.append(lower)
#        lower = lower + 1
#    return myList
        

#upper = 10
#myList = myRange(upper)
#print(myList)

#print(myRange(10))


def myRange(start = None, stop = None, reverse = None):
    if (stop == None) and (reverse == None):
        myList = []
        stop = 0
        while  stop < start:   
            myList.append(stop)
            stop = stop + 1
        return myList
    else:
        if start > stop:
            myList = []
            while stop < start:
                myList.append(start)
                start = start + reverse
            return myList
    
        else:
            myList = []
            while start < stop:
                myList.append(start)
                start = start + reverse
            return myList
    
        

print(myRange(10))
#[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
print(myRange(10,1,-1))
#[10, 9, 8, 7, 6, 5, 4, 3, 2])
print(myRange(1,10,2))
#[1, 3, 5, 7, 9]
print(myRange(4,12,2))
#[4, 6, 8, 10]

