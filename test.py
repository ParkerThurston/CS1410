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
temp_list = []
def compute_mode(my_list):
    counts = {}
    maxcount = 0
    for number in my_list:
        if number not in counts:
            counts[number] = 0
        counts[number] += 1
        if counts[number] > maxcount:
            maxcount = counts[number]

    for number, count in counts.items():
        if count == maxcount:
            temp_list.append(number)

num_count = [3, 1, 7, 1, 4, 10] #any list
compute_mode(num_count)
print('Mode:' + str(temp_list))
