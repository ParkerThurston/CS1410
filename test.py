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
   
# def report():
#    a = StringIO()
#    for name in sorted(similarities.keys()):
#        print(name+ ":", friends(name), file=s)
#        for b in recomend(name):
#            print('\t ',b, file = s)

#teacher code

#print(reduce(max, [34, 21, 99, 67, 10]))

#print("test \nfjowefj")
# resp = input("Your command: ")

# resp = resp.split()

# if resp[0] == "quit":
#     pass
#     #return False
# if resp[0] == "cancel":
#     pass
# elif resp[0] == "insert":
#     if resp [1] == 50 or 25 or 10 or 5:
#         credit = resp[1]
#         print(credit)
#         #return credit
# elif resp[0] == "select":
#     pass
#     #if self.cashBox.credit < self.selector.# ??? price
# else:
#     print("Invalid entry")



# class Selector:
#     def __init__(self, cashbox):
#         self.cashBox = cashbox
#         self.prod = CoffeeMachine()
        
        

#     def select(self):
#         product = self.prod.products 
#         print(product)
        

# class CoffeeMachine:
#     def __init__(self):
#         self.totalC = 0.0
#        # self.cashBox = CashBox()
#         self.products = ["1","2","3"]
#         #products.append(Product("Black", 35, "Making black: \nDispensing cup \nDispensing coffee \nDispensing water"))
#         #self.selector = Selector(self.cashBox)

# def Main():
#     F = Selector(100)
#     F.select()

# if __name__ == "__main__":
#     Main()


# resp = input("put Price:")
# resp = resp.split()
# print(resp[3])

# products = {"black": "35", "white": 35, "sweet": 35, "white & sweet": 35, "bouillon": 25}

# print(products)
# print(products["black"])

# lyst = ["Richard Adams, Watership Down",
# 	"F. Scott Fitzgerald, The Great Gatsby",
# 	"William Golding, Lord of the Flies"
# 	"William Goldman, The Princess Bride",
# 	"Daniel Keyes, Flowers For Algernon",
# 	"Garth Nix, Sabriel",
# 	"Jodi Picoult, My Sister's Keeper",
# 	"J R R Tolkien, The Lord of the Rings"]
# Alyst = []
# for i in range(len(lyst)):
#     print("\t" + lyst[i] + ", " + lyst[i])

#print(Alyst)


       
# lyst = [1,2,3,4]

# for i in range(len(lyst)):
# 	print(lyst[i])

# def main():
#     myCount = Count()
#     times = 0

#     for i in range(0, 100):
#         increment(myCount, times)

#     print("myCount.count =", myCount.count, "times =", times)

# def increment(c, times):
#     c.count += 1
#     times += 1

# class Count:
#     def __init__(self):
#         self.count = 0
    
# main()

# import matplotlib.pyplot as plt 

# plt.plot([1,2,3,10])
# plt.ylabel("y label")
# plt.show()


# count = 0
# while count < 100:
#      # Point A
#      print("Welcome to Python!")
#      count += 1
#      # Point B

# print(count)

# m = [[x, x + 2, x + 1] for x in range(1, 9, 3)]
# print(m)

# points = [[1, 2], [3, 1.5], [0.5, 0.5]]
# points.sort()
# print(points)

# d = {"john":40, 25:"peter"} 
# d = { }
# d = {40:"john", 45:"peter"}  
# d = (40:"john", 45:"peter") 

class A:
    def __init__(self):
        self.setI(10)

    def setI(self, i):
        self.i = 2 * i;

class B(A):
    def __init__(self):
        super().__init__()
        print("i from B is", self.i)
        
    def setI(self, i):
        self.i = 3 * i;

b = B()