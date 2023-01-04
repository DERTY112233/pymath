#!/bin/python3

import math

kmp = float(input("Enter speed in kmph: "))

def mps(kmp):
    mps = (kmp*1000)/3600
    print("The speed in m/s is ", round(mps))

mps(kmp)

