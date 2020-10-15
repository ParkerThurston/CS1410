#This Code was written by Parker Thurston, with help from code that was done in class


from heapq import nlargest
from operator import itemgetter

#read booklist
with open("booklist.txt") as BookL:
    books = [tuple(line.strip().split(",")) for line in BookL]

#read ratings
with open("ratings.txt") as RatingL:
    ratings = {}
    NList = []
    while True:
            names = RatingL.readline().strip().lower()
            if not names:
                break
            scores = RatingL.readline().strip().split()
            ratings[names] = [int(n) for n in scores]
            NList.append(names)
    NList.sort()


def dotprod(x, y):

    assert len(x) == len(y)
    return sum(x[i]*y[i] for i in range(len(x)))



def compute_scores():
    similarities = {}
    for name1 in ratings:
        for name2 in ratings:
                if name1 != name2:
                    affinityScore = dotprod(ratings[name1], ratings[name2])
                    if affinityScore > 0:
                            similarities[name1] = similarities.get(name1, {})
                            similarities[name1][name2] = affinityScore
    return similarities





def friends(name):
    similarities = compute_scores()
    afResults = similarities[name]
    topTwo = [name for name, _ in nlargest(2,afResults.items(),key=itemgetter(1))]
    return sorted(topTwo)
   



def recommend(name, topTwo):
    recList = []
    def aut_title(books):
        aut = books[0].split()
        return(aut[-1],aut[0],books[1])

    for i in range(len(books)):
        if ((ratings[name][i] == 0) and ((ratings[topTwo[0]][i] > 2) or (ratings[topTwo[1]][i] > 2))):
            recList.append(books[i])
    return sorted(recList,key=aut_title)





def report():
    f = open("AllRecomends.txt", 'w')
    for i in range(len(NList)):
        NlistTOP2 = friends(NList[i])
        f.write("\nRecommendations for " + NList[i] + " from " + NlistTOP2[0] +" and " + NlistTOP2[1]+":")
        compute_scores()
        ANrecList = recommend(NList[i], NlistTOP2) 
        for i in range(len(ANrecList)):
            f.write("\n\t" + ANrecList[i][0] + ", " + ANrecList[i][1])
        




def main():
    report()
    testName = input("Enter a readers name: ")

    if testName in ratings.keys():
        name = testName
    else:
        print(testName + " is not a name in the list")
        exit()
    
    topTwo = friends(name)
    print("Recommendations for " + name + " from " + topTwo[0] +" and " + topTwo[1])
    compute_scores()
   
    recList = recommend(name, topTwo) 
    for i in range(len(recList)):
        print("\t" + recList[i][0] + ", " + recList[i][1])



if __name__ == "__main__":
    main()


