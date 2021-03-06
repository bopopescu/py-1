#!/usr/bin/env python

#    Created by: Noe Quintero
#    E-mail: nquintero@linear.com
#
#    REVISION HISTORY
#    $Revision: 2581 $
#    $Date: 2014-06-26 15:51:36 -0700 (Thu, 26 Jun 2014) $

#    Copyright (c) 2013, Linear Technology Corp.(LTC)
#    All rights reserved.

#    Redistribution and use in source and binary forms, with or without
#    modification, are permitted provided that the following conditions are met:

#    1. Redistributions of source code must retain the above copyright notice, this
#       list of conditions and the following disclaimer.
#    2. Redistributions in binary form must reproduce the above copyright notice,
#       this list of conditions and the following disclaimer in the documentation
#       and/or other materials provided with the distribution.

#    THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS" AND
#    ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED
#    WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE
#    DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT OWNER OR CONTRIBUTORS BE LIABLE FOR
#    ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES
#    (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES;
#    LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND
#    ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT
#    (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE OF THIS
#    SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.

#    The views and conclusions contained in the software and documentation are those
#    of the authors and should not be interpreted as representing official policies,
#    either expressed or implied, of Linear Technology Corp.

from dc590 import *
from packets import *

# Write data to the Avalon bus
def transaction_write(dc590, base, write_size, data):
    # Create the packet
    packet = create_packet(CONST_SEQUENTIAL_WRITE, write_size, base, data)
    # Convert to DC590 string
    packet = packet_to_DC590(packet, 4)
    # Send/receive packets via DC590
    data_packet = dc590.transfer_packets(packet, 4)
    # Convert DC590 return packet string to int list 
    data_packet = DC590_to_packet(data_packet)
    # Decode packet to data
    data = packet_to_data(data_packet)
    return data

# Reads data to the Avalon bus
def transaction_read(dc590, base, read_size):
    # Create the packet
    packet = create_packet(CONST_SEQUENTIAL_READ, read_size, base)
    #print packet
    # Convert to DC590 string
    packet = packet_to_DC590(packet, read_size)
    #print packet
    # Send/receive packets via DC59
    data_packet = dc590.transfer_packets(packet, read_size)
    # Convert DC590 return packet string to int list 
    data_packet = DC590_to_packet(data_packet)
    # Decode packet to data
    data = packet_to_data(data_packet)
    return data
    
#*************************************************
# Function Tests
#*************************************************

if __name__ == "__main__":
    
    try:
        dc590 = DC590() # Look for the DC590
        
        print transaction_write(dc590, 0, 1, [0xF])
        print transaction_read(dc590, 0, 1)
         
    finally:
        dc590.close()
    print "Test Complete"