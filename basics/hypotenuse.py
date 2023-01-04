#!/bin/python3

import math
from time import sleep

a = int(input("Enter for a: "))
b = int(input("Enter for b: "))

def hypotenuse(aheight, blen):
    print("PROCESSING.........")
    sleep(2)
    a = aheight**2
    b = blen**2
    newab = a + b
    print(math.sqrt(newab))

hypotenuse(a,b)
