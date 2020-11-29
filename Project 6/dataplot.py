import glob
import numpy as np
import matplotlib.pyplot as plt
import array as arr

def analyze(fname):
    #Read the raw data
    raw_data = np.loadtxt(fname)
    #smooth raw data
    smooth_data = smooth(raw_data)
    

    #Find pulses
    pulses = []
    vt = 100
    for i in range(len(smooth_data)-2):
        if (smooth_data[i + 2] - smooth_data[i]) > vt:
            pulses.append(i)

            #skip until the sample begins to decrease
            i += 1
            while i < len(smooth_data) and smooth_data[i+1] > smooth_data[i]:
                i+= 1
    
    #plot the data
    _,axes = plt.subplots(nrows=2)
    axes[0].plot(raw_data)
    axes[0].set(title=fname, ylabel="Raw", xticks= [])
    axes[1].plot(smooth_data)
    axes[1].set(ylabel="Smooth")
    #plt.show()

    pdf_file = fname[:-3] +"pdf"
    plt.savefig(pdf_file)
    # Calculated area and write to file


    # area = 0
    # k = 0
    # for i in range(len(pulses)-1):
    #     while (pulses[i+k] < pulses[i+1]):
    #         area = raw_data[i]
    #         k+=1
        
    #     print( i +"    ("+area+")")
    #     i+=1



    pulse_end = pulses[-2]
    k = 0
    pulse_area = 0


    for i in pulses:
        if i != pulse_end:
            var = pulses[k+1]
            while( i < var):
                pulse_area += raw_data[i]
                i+=1
            k+=1
            
    

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





