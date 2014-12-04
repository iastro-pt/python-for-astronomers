from __future__ import division
import numpy as np
import numpy.random as rnd
from numpy import pi
from scipy.integrate import quad


## Estimate pi by numerical integration

def integrand1(t):
    """ integrate sin(t)**2 / t**2 over range 0-inf to obtain pi/2 """
    return ((np.sin(t))**2) / t**2


def integrand2(t):
    """ integrate 4*sqrt(1-t^2) over 0-1 to obtain pi """
    return 4 * np.sqrt(1 - t**2)

def integrand9(t):
    """ integrate 40/11 * (sin(t)/t)^6 over range 0-inf to obtain pi """
    return 40 / 11 * (np.sin(t) / t)**6


pi_estimate1 = 2*quad(integrand1, 0, np.Inf)[0]
pi_estimate2 = quad(integrand2, 0, 1)[0]
pi_estimate3 = quad(integrand9, 0, np.Inf)[0]

print 'estimated pi (int1) = ' ,'%0.16f' % (pi_estimate1)
print 'estimated pi (int2) = ' ,'%0.16f' % (pi_estimate2)
print 'estimated pi (int3) = ' ,'%0.16f' % (pi_estimate3)


## Estimate pi by Monte Carlo simulation

def estimate_pi1(npoints=1e5):
    """ Estimates pi taking area ratio between a circle and a square
    Generates uniformly distributed corrdinates using Numpy.random over -1:1.
    This uses radius of the circle to be 1 so the side of square = 2.
    Determines points inside the circle using a mask."""

    x = 2*rnd.rand(1,npoints)-1 # random array between -1 and +1
    y = 2*rnd.rand(1,npoints)-1 # random array between -1 and +1

    mask = [(x ** 2 + y ** 2) ** 0.5 < 1]

    pi_est = 4 * np.sum(mask) / np.size(mask)

    return pi_est


def estimate_pi2():
    # Generating 10000 random points in a unit square
    x = np.random.uniform(-1.0, 1.0, 10000)
    y = np.random.uniform(-1.0, 1.0, 10000)

    # Counting the random points inside the unit circle inscribed in the square
    inside = 0
    n = 10000

    for i in range(0,len(x)-1):
        if np.sqrt(x[i]**2+y[i]**2)<=1:
            inside = inside + 1
        else:
            pass

    # Estimating pi
    pi_estimate = 4.0*inside/n

    return pi_estimate


def estimate_pi3(relerror=0.001):
    """ Estimates pi taking area ratio between a circle and a square.
    Generates uniformly distributed corrdinates using random over 0:1 and determines
    points inside the circle using math.hypot.
    Returns estimate of pi and total number of iterations."""
    import random
    import math

    count_inside = 0
    count_total = 0
    while True:
        d = math.hypot(random.random(), random.random())
        if d < 1:
            count_inside += 1
        count_total += 1
        pi_est = 4.0 * count_inside / count_total
        if abs((pi_est/pi)-1) <= relerror:
            break
    return pi_est, count_total


print 'estimated pi (MC1) = %0.16f' % estimate_pi1()
print 'estimated pi (MC2) = %0.16f' % estimate_pi2()
print 'estimated pi (MC1) = %0.16f  (iter=%d)' % estimate_pi3()


print '\nreal pi = ' , '%0.16f' % pi
