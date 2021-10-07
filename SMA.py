# -*- coding: utf-8 -*-
"""
Created on Tue Oct  5 16:25:16 2021

@author: tanka
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


def getMovingAverage(data, window=int):
    weights = np.repeat(1.0, window) / window
    smas = np.convolve(data, weights, 'valid')
    return smas


# Make both SMAs the same length
def balanceLengths(sma1, sma2):
    sma1 = sma1 if len(sma1) <= len(sma2) else sma1[len(sma1)-len(sma2):]
    sma2 = sma2 if len(sma2) <= len(sma1) else sma2[len(sma2)-len(sma1):]
    return sma1, sma2


def getCrossovers(sma1, sma2):
    # Compare SMA1 and SMA2 by computing SMA1 - SMA2.If the difference is positive
    # it indicates that SM1 is above SMA2 (1), and vice versa (0)
    # resulting arr is a sequence of 0's and 1's
    diff = sma1-sma2
    arr = [1 if x >= 0 else 0 for x in diff]

    # ax.plot(range(len(sma15)), arr, label='arr')

    # Compute the difference of each pair of consevutive numbers
    # in the above mentioned sequence of 0's and 1's.
    # Resulting arr1 is a sequence of values of 0, 1 and -1

    arr1 = [arr[i]-arr[i+1] for i in range(len(arr)-1)]
    # Insert a non-crossover point at the first index
    arr1.insert(1, 0)

    return arr1

# Find the locations of 1's and -1's, these are the crossovers


def main():
    df = pd.read_csv("PLTR.csv")  # this is received from API

    closeData = df["Close"]

    sma15 = getMovingAverage(closeData, 15)
    sma50 = getMovingAverage(closeData, 50)

    sma15, sma50 = balanceLengths(sma15, sma50)
    crossovers = getCrossovers(sma15, sma50)

    # fig, ax = plt.subplots()
    # ax.plot(range(len(sma15)), sma15, label='sma15')
    # ax.plot(range(len(sma15)), sma50, label='sma50')
    # ax.plot(range(len(sma15)), crossovers, label='cross')

    # ax.set_xlabel('days')
    # ax.set_ylabel('price')
    # ax.legend()


if __name__ == "__main__":
    main()
