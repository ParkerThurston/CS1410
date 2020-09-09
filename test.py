#rating = "0 1 3"
#fixedrat = rating.strip().split(" ")
#print(fixedrat)


#rating2 = "0 1 -3"
#fixedrat = rating2.strip().split(" ")
#print(fixedrat)

##fruits = ["apple", "banana", "cherry"]
#for [x] in rating[]:
    
#  print(x)
#x = [1, 3]
##y = [4, 0]
#def dot(x,y):
    
#    assert len(x) == len(y)    
#    return sum(x[i]*y[i] for i in range(len(x)))
#print(dot(x,y))

##list= [input("list:")]
#print(list)
#temp_list = []
#def compute_mode(my_list):
#    counts = {}
#    maxcount = 0
#    for number in my_list:
#       if number not in counts:
#            counts[number] = 0
#        counts[number] += 1
#        if counts[number] > maxcount:
#            maxcount = counts[number]
#
#    for number, count in counts.items():
#        if count == maxcount:
#            temp_list.append(number)

from heapq import nlargest
from operator import itemgetter


dict = {'now': 1, 'is': 1, 'the': 2, 'time': 1, 'for': 1, 'all': 1, 'good': 1, 'men': 1, 'to': 2, 'come': 1, 'aid': 1, 'of': 1, 'their': 1, 'country': 1} 
print(nlargest(2,dict.items(),key=itemgetter(1)))


