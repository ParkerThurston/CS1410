#Code written by Parker Thurston, with help from class code (With some extra help from Hannah Young and John Mittelstaedt)

from time import perf_counter
import requests

# Download a flag from the CIA
prefix = 'https://www.cia.gov/library/publications/resources/the-world-factbook/graphics/flags/large/'
    # Note: No headers={...}

 

def Flags(flagLyst):
    bitties = 0 
    for ch in flagLyst:
        fname = prefix + ch + "-lgflag.gif"
        flag = requests.get(fname).content
        file_name = "flags/" + ch + ".gif"
        with open(file_name,"wb") as f:
            f.write(flag)
        bitties += len(flag)
    return bitties
    


def main():
    with open("flags.txt") as f:
        flagL = [line.strip() for line in f]

    start = perf_counter()
    Fullbitties = Flags(flagL)
    stop = perf_counter()
    with open("Output.txt", "a") as f:
        f.write("CIA_A: Outputs \n")
        f.write("Elapsed Time: " + str(stop - start) + " seconds \n")
        f.write( str(Fullbitties) + " bytes downloaded \n")
    
if __name__ == "__main__":
    main()

