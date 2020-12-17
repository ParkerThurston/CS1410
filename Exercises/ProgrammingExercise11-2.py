"""
File: reverse.py
Project 11.2

Defines a function to reverse the elements in a list.
"""

def reverse(lyst):
    # lyst2 = lyst.copy()
    lyst = lyst[::-1]
    return lyst
    

def main():
    """Tests with two lists."""
    lyst = list(range(4))
    reverse(lyst)
    print(lyst)
    lyst = list(range(3))
    reverse(lyst)
    print(lyst)

if __name__ == "__main__":
    main()



