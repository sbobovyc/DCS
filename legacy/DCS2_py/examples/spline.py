#! /bin/env python2.6

import numpy as np
import matplotlib.pyplot as plt
from scipy import interpolate, randn

x = np.arange(0,5,1.0/6)
xs = np.arange(0,5,1.0/500)

y = np.sin(x+1) + .2*np.random.rand(len(x)) -.1

knots = np.array([1,2,3,4])
tck = interpolate.splrep(x,y,s=0,k=3,t=knots,task=-1)
ys = interpolate.splev(xs,tck,der=0)

plt.figure()
plt.plot(xs,ys)


plt.show()
