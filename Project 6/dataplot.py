#Code written by Parker Thurston with help from Class (With some extra help from Hannah Young and John Mittelstaedt)

import glob
import numpy as np
import matplotlib.pyplot as plt


def analyze(fname):
    # Read the raw data
    raw_data = np.loadtxt(fname)
    # Smooth raw data
    smooth_data = smooth(raw_data)
    

    # Find pulses
    pulses = []
    vt = 100
    index_p = 0
    for i in range(len(smooth_data)-2):
        if (smooth_data[i + 2] - smooth_data[i]) > vt:
            if i > index_p:
                pulses.append(i)

            # Skip until the sample begins to decrease
            i += 1
            while i < len(smooth_data) and smooth_data[i+1] > smooth_data[i]:
                i+= 1
                index_p = i
    
    # Plot the data
    _,axes = plt.subplots(nrows=2)
    axes[0].plot(raw_data)
    axes[0].set(title=fname, ylabel="Raw", xticks= [])
    axes[1].plot(smooth_data)
    axes[1].set(ylabel="Smooth")
    #plt.show()

    pdf_file = fname[:-3] +"pdf"
    plt.savefig(pdf_file)
    # Calculated area and write to file

    pulse_end = pulses[-1]
    k = 0
    pulse_area = 0
    Maxwidth=50
    width = 0
    pulse_areaL = []

    for p in pulses:
        if p != pulse_end:
            var = pulses[k+1]
            while( p < var):
                pulse_area += raw_data[p]
                p+=1
            k+=1
            pulse_areaL.append(pulse_area)
            pulse_area = 0
        else:
            while( width < Maxwidth):
                pulse_area += raw_data[p]
                p+=1
                width+=1
            pulse_areaL.append(pulse_area)
            pulse_area = 0
    
    # Writing to a file 

    out_file = fname[:-3] +"out"
    with open(out_file, "w") as file1: 
        file1.write(fname + ":     \n")
        for L in range(len(pulses)):
            file1.writelines("Pulse " + str(L+1) + ": " + str(pulses[L])+ "  (" + str(int(pulse_areaL[L]))+ ")\n") 
    
    

def smooth(data):
    '''smoothing filter
        returns a smoothied copy of the input
    '''
    res = data.copy()

    for i in range(3, len(data)-3):
        res[i] = (data[i-3] + 2 * data[i-2] + 3 * data[i-1] + 3 * data[i] + 3* data[i+1] + 2 *data[i+2] + data[i+3]) // 15

    return res


def main():
    for fname in glob.glob('*.dat'):
        analyze(fname)
    

if __name__ == "__main__":
    main()





