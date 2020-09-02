
with open("booklist.txt") as BookL:
    books = [tuple(line.strip().split(",")) for line in BookL]


with open("ratings.txt") as RatingL:
    ratings = {}
    while True:
            names = RatingL.readline().strip().lower()
            scores = RatingL.readline().split()
            if not scores:
                break
            ratings[names] = [int(n) for n in scores]


def dotprod(x,y):

    assert len(x)==len(y)
    return sum(x[i]*y[i] for i in range(len(x)))




#def getAfinityScore():

