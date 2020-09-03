#read booklist
with open("booklist.txt") as BookL:
    books = [tuple(line.strip().split(",")) for line in BookL]

#read ratings
with open("ratings.txt") as RatingL:
    ratings = {}
    while True:
            names = RatingL.readline().strip().lower()
            if not names:
                break
            scores = RatingL.readline().strip().split()
            ratings[names] = [int(n) for n in scores]


def dotprod(x, y):

    assert len(x) == len(y)
    return sum(x[i]*y[i] for i in range(len(x)))

similarities = {}

def compute_scores():
   for name1 in ratings:
        for name2 in ratings:
                if name1 != name2:
                    affinityScore = dotprod(ratings[name1], ratings[name2])
                    if affinityScore > 0:
                            similarities[name1] = similarities.get(name1, {})
                            similarities[name1][name2] = affinityScore

compute_scores()

def friends(name):
   #affinityScore = similarities[name]
   pass

print(books)
print(ratings)

def main():
   #friends("ben")
   print(books)
   print(ratings)



if __name__ == "__main__":
    pass


