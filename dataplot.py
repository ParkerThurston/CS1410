import glob
import numpy as np

def analyze(fname):
    #Read the raw data
    raw_data = np.loadtxt(fname)
    #smooth raw data
    smooth_data = smooth(raw_data)

    #Find pulses

    #plot the data

    # Calculated area and write to file


    #len(raw_data)

def smooth(data):
    '''smoothing filter
        returns a smoothied copy of the input
    '''
    res = data.copy()

    for i in range(3, len(data)-3):
        res[i] = (data[i-3] +2 * data[i-2] +3 * data[i-1] + 3 * data[i] + 3* data[i+1} + 2])

def main():
    for fname in glob.glob('*.dat'):
        analyze(fname)

def if __name__ == "__main__":
    main():