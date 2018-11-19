"""
Author: Cassidy Skorczewski
Project: CS356 Honors Project
"""

#Elliptical Curve Cryptography

import numpy as np
import random
from matplotlib import pyplot as plt

def ellipticalCurve(y, x, a, b):
    """This function plots the point of the function y^2=x^3+ax+b"""
    
    return pow(y, 2) - pow(x, 3) - x * a - b

def selectCoeff():
    """This function selects the a and b coeff for the elliptical curve"""
    
    a = random.randint(-11,11)
    b = random.randint(-11,11)
    
    if (4*(a**3) + 27*(b**2)) == 0:
        print("Invalid choice of a and b. Try Again.")
        exit
    
    return a, b

def findGeneratorPt(a, b):
    """This function selects a Generator Pt on the function"""
    
    x = random.uniform(-2, 4)
    y = np.sqrt(pow(x,3) + x*a + b)
    factor = random.choice([-1,1])
    return x, factor*y

def ptDoubling(Gx, Gy, a):
    """This function returns 2P = P + P"""
    
    s = (3 * pow(Gx, 2) + a) / (2 *Gy)
    Px = pow(s,2) - (2 * Gx)
    Py = s*(Gx-Px) - Gy
    return Px, -Py, Py

def plotCurve(a,b, Ptx, Pty, nPy):
    y, x = np.ogrid[-5:5:100j, -5:5:100j]
    plt.contour(x.ravel(), y.ravel(), ellipticalCurve(y,x,a,b), [0])
    plt.scatter(Ptx[0], Pty[0], label="P")
    plt.scatter(Ptx[1], Pty[1], label="-2P")
    plt.scatter(Ptx[1], nPy, label="2P")
    plt.plot(Ptx, Pty)
    plt.plot([Ptx[1], Ptx[1]], [Pty[1], nPy], "--")
    
    plt.title("Elliptical Curve Graph where a={0} and b={1}".format(a,b))
    plt.axhline(0, color='black')
    plt.axvline(0, color='black')
    plt.legend()
    plt.grid()
    plt.show()
    
if __name__ == "__main__":
    #a, b = selectCoeff()
    a, b = -6, 9
    Gx, Gy = findGeneratorPt(a, b)

    Px, Py, nPy = ptDoubling(Gx, Gy, a)
    Ptx, Pty = [Gx, Px], [Gy, Py]
    plotCurve(a, b, Ptx, Pty, nPy)
    
    