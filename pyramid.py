#Code written by Parker Thurston with help from class code

import sys
from time import perf_counter

WEIGHT = 200
cache = {}

numberofFunctionCalls = 0
numberOfCacheCalls = 0

def weightOn(r,c):
    global numberofFunctionCalls  
    numberofFunctionCalls += 1

    if (r,c) in cache:
        global numberOfCacheCalls  
        numberOfCacheCalls += 1
        return cache[(r,c)]

    if r == 0:
        result = 0.0
    elif c == 0:
        result = (WEIGHT + weightOn(r - 1,c))/2.0
    elif r == c:
        result = (WEIGHT + weightOn(r - 1,c - 1))/2.0 
    else:
        result = WEIGHT + (weightOn(r - 1,c - 1) + weightOn(r - 1,c))/2.0
    
    cache[(r,c)] = result

    return result

    


def main():
    #if len(sys.argv) < 2:
    #    print("Error: argument not passed into program")
    #    return

    rows = int(sys.argv[1])
   
    # with open("part2.txt", 'w') as f:
    #     start = perf_counter()

    #     for i in range(rows):
    #         for j in range(i + 1):
    #             print(f'{weightOn(i, j):.2f}', file=f, end=" ")
    #         print("\n",file=f)
       
    #     end = perf_counter()

    #     print(f"Elapsed Time: {end - start} seconds", file = f)
    #     print(f"Number of function calls: {numberofFunctionCalls}", file = f)
    #     print(f"Number of cache hits: {numberOfCacheCalls}",file = f)

    with open("part3.txt", 'w') as f:
        start = perf_counter()

        for i in range(rows):
            for j in range(i + 1):
                print(f'{weightOn(i, j):.2f}', file=f, end=" ")
            print("\n",file=f)
       
        end = perf_counter()

        print(f"Elapsed Time: {end - start} seconds", file = f)
        print(f"Number of function calls: {numberofFunctionCalls}", file = f)
        print(f"Number of cache hits: {numberOfCacheCalls}",file = f)
if __name__ == "__main__":
    main()


