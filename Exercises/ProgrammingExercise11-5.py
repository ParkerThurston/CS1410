def selectionSort(lyst, reverse = False):
    """Sorts the items in lyst in ascending order."""
    if reverse == False:
        i = 0
        while i < len(lyst) - 1: # Do n – 1 searches
            minIndex = i # for the smallest item
            j = i + 1
            while j < len(lyst): # Start a search
                if lyst[j] < lyst[minIndex]:
                    minIndex = j
                j += 1
            if minIndex != i: # Swap if necessary
                swap(lyst, minIndex, i)
            i += 1
    if reverse == True:
        i = 0
        while i < len(lyst) - 1: # Do n – 1 searches
            maxIndex = i # for the smallest item
            j = i + 1
            while j < len(lyst): # Start a search
                if lyst[j] > lyst[maxIndex]:
                    maxIndex = j
                j += 1
            if maxIndex != i: # Swap if necessary
                swap(lyst, maxIndex, i)
            i += 1

def swap(lyst, x, y):
    """Exchanges the elements at positions x and y."""
    lyst[x], lyst[y] = lyst[y], lyst[x]
        
def main():
    """Tests with four lists."""
    lyst = [2, 4, 3, 0, 1, 5]
    selectionSort(lyst)
    print(lyst)
    lyst = list(range(6))
    selectionSort(lyst)
    print(lyst)
    lyst = [2, 4, 3, 0, 1, 5]
    selectionSort(lyst, reverse = True)
    print(lyst)
    lyst = list(range(6))
    selectionSort(lyst, reverse = True)
    print(lyst)

if __name__ == "__main__":
    main()

    

