# test_ltccap.py - An example program to test the Python LtcCap
#
# Copyright (c) 2011 Linear Technology Corporation
# This software is property of Linear Technology Corporation (LTC) and is being provided for 
# example purposes only. Sale or redistribution of this software or any of its parts requires 
# prior written permission from LTC.
# This software is provided AS IS, and WITHOUT WARRANTY OF ANY KIND, by using this software you
# agree that LTC is not responsible for any damages of any kind directly or indirectly related
# to the possesion or use of this software.
# 
# Created by Jeremy Sorensen; jsorensen@linear.com
# Dec 02, 2011
# $ LastChangedBy: $
# $ Date: $
# $ Revision: $

# Hacked by Mark Thoren - experimenting with basic number crunching / Matplotlib.

# import the ltccap module
from ltccap import *
from matplotlib import pyplot as plt
import numpy as np
from scipy import fft, arange

# number of samples to read
NSAMPS = 16384

# Create the LtcCap object representing the ADC, passing in the parameters
# NOTE: This is probably wrong for your setup, change these parameters to match your setup
# adc = LtcCap.create(DC718, 1, 16, 16, True, POS_EDGE, CMOS)

# Create the LtcCap object representing the ADC, allowing the user to enter the device
# parameters interactively through a dialog box

#    adc = LtcCap.createFromDialog() #Use this to prompt with form
adc = LtcCap.create(DC718, 1, 16, 16, BIPOLAR, 1, NONE)
#    adc = LtcCap.create(DC890, 2, 16, 16, BIPOLAR, 1, CMOS)



again = 'y'
while(again == 'y'):
    try:

        # read NSAMPS points
        if adc.nChannels == 2:
            # two channel read
            data1, data2 = adc.read(NSAMPS, IMMEDIATE)
            # now print the data
    #        print("Data: ")
    #        for i in range(len(data1)):
    #            print("" + str(data1[i]) + "," + str(data2[i]))
            data = data1
        else:
            # single channel read
            data = adc.read(NSAMPS, IMMEDIATE)
    
    
        #now print the data
        print 'First 16 points of Data: '
        #for d in (0:15):
        #    print(d)
        print data[0:15]        
        print type(data)
        x=np.array(range(0, NSAMPS)[:])
        y = np.array(data[0:NSAMPS])
    
        print "X's type"
        print type(y)
        print "X's shape"
        print x.shape
        print "X's length"
        print x.size
    
        print "Y's type"
        print type(y)
        print "Y's shape"
        print y.shape
        print "Y's length"
        print y.size
    
    #    x=np.zeros(128)
    #    x[10]=1
        z = np.array(NSAMPS)
        window = np.blackman(NSAMPS)
 #       window = np.ones(NSAMPS)
        z = y * window

        figure(1)    
        plt.plot(x, log(abs(fft(z))))
    #    plt.plot(x, y)    
        plt.title('Freq Domain')
        plt.xlabel('X Axis Label')
        plt.ylabel('Y Axis Label')

        plt.show()
        figure(2)
        plt.plot(window)
        plt.show()
#        again = raw_input('type y to take another sample, any other to exit')
        again = 'n'

    except LtcCapError as e:
        print("Error: " + e.value)


