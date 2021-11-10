import numpy as np
import matplotlib.pyplot as plt


def getMovingAverage(data, window=int):
    weights = np.repeat(1.0, window) / window
    smas = np.convolve(data, weights, 'valid')
    return smas


# Make both SMAs the same length
def balanceLengths(sma1, sma2):
    sma1 = np.concatenate((np.array([np.nan]*(len(sma2)-len(sma1))),
                          sma1)) if len(sma1) <= len(sma2) else sma1
    sma2 = np.concatenate((np.array([np.nan]*(len(sma1)-len(sma2))),
                          sma2)) if len(sma2) <= len(sma1) else sma2
    return sma1, sma2


def getCrossovers(sma1, sma2):
    # Compare SMA1 and SMA2 by computing SMA1 - SMA2.If the difference is positive
    # it indicates that SM1 is above SMA2 (1), and vice versa (0)
    # resulting arr is a sequence of 0's and 1's
    diff = sma1-sma2
    # arr = [1 if x >= 0 else 0 for x in diff]
    arr = list(map(lambda x: 1 if x >= 0 else 0, diff))

    # ax.plot(range(len(sma15)), arr, label='arr')

    # Compute the difference of each pair of consevutive numbers
    # in the above mentioned sequence of 0's and 1's.
    # Resulting arr1 is a sequence of values of 0, 1 and -1

    arr1 = [arr[i]-arr[i+1] for i in range(len(arr)-1)]
    # Insert a non-crossover point at the first index
    arr1.insert(1, 0)

    # Remove the first -1/1 that is caused by a nan value
    for i in range(len(arr1)):
        if arr1[i] != 0:
            arr1[i] = 0
            break

    return arr1

# Find the locations of 1's and -1's, these are the crossovers


def getSMAPlots(closeData, window1, window2):
    sma1 = getMovingAverage(closeData, window1)
    sma2 = getMovingAverage(closeData, window2)

    sma1, sma2 = balanceLengths(sma1, sma2)
    crossovers = getCrossovers(sma1, sma2)
    if window1 < window2:
        crossBuy = [1 if x == 1 else 0 for x in crossovers]
        crossSell = [-1 if x == -1 else 0 for x in crossovers]
    else:
        crossSell = [1 if x == 1 else 0 for x in crossovers]
        crossBuy = [-1 if x == -1 else 0 for x in crossovers]
    return sma1, sma2, crossBuy, crossSell
