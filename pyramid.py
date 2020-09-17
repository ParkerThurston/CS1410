import sys

WEIGHT = 200

def weightOn(r,c):
    if r == 0:
        result = 0.0
    elif c == 0:
        result = (WEIGHT + weightOn(r - 1,c))/2.0
    elif r == c:
        result = (WEIGHT + weightOn(r - 1,c - 1))/2.0 
    else:
        result = WEIGHT + (weightOn(r - 1,c - 1) + weightOn(r - 1,c))/2.0
    return result


def main():
    #if len(sys.argv) < 2:
    #    print("Error: argument not passed into program")
    #    return
    #rows = int(sys.argv[1])
    #column = sys.argv[2] #NOT ACTUALLY NEEDED AT FINAL
    
    row = 3
    column = 1
    print(f'{weightOn(row, column):.2f}')


if __name__ == "__main__":
    main()


