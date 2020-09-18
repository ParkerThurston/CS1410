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

#from heapq import nlargest
#from operator import itemgetter


#dict = {'now': 1, 'is': 1, 'the': 2, 'time': 1, 'for': 1, 'all': 1, 'good': 1, 'men': 1, 'to': 2, 'come': 1, 'aid': 1, 'of': 1, 'their': 1, 'country': 1} 
#print(nlargest(2,dict.items(),key=itemgetter(1)))


#def checkKey(dict, key): 
      
#    if key in dict.keys(): 
#        print("Present, ", end =" ") 
#        print("value =", dict[key]) 
#    else: 
#        print("Not present") 
  
# Driver Code 
#dict = {'a': 100, 'b':200, 'c':300} 
  
#key = 'b'
#checkKey(dict, key) 
  
#key = 'w'
#checkKey(dict, key) 

#from io import StringIO
#def recomend(name1):

#    def aut_title(books):
#        aut = books[0].split()
#        return(aut([-1],aut[0],books[1]))
#
#    read1=(i for i in range(len(books)) if ratings[name1] [i] != 0) 
#    recs = set()
#    for name2 in friends(name1):
#        liked2 = (i for i in range(len(books)) if ratings[name2] [i] > 1)
#        recs |= liked2 - read1
#    good_books = [books[i] for i in recs]
#    return sorted(good_books,key=aut_title)
#    
#def report():
#    a = StringIO()
#    for name in sorted(similarities.keys()):
#        print(name+ ":", friends(name), file=s)
#        for b in recomend(name):
#            print('\t ',b, file = s)

#teacher code

#print(reduce(max, [34, 21, 99, 67, 10]))

