# -*- coding: utf-8 -*-
"""
Created on Fri Aug 20 16:34:24 2021

@author: rober
"""

import serial  # 引用pySerial模組
import time

# db
from db_wrapper import DBWrapper

import urllib.request
import urllib.error


# wait for internet connection
def connect(host='http://google.com'):
    try:
        urllib.request.urlopen(host) #Python 3.x
        return True
    except urllib.error.URLError:
        print('not connected to internet')
        return False


while True:
    if connect():
        break
    time.sleep(5)


db = DBWrapper()


# SDS011
import struct
from datetime import datetime

# Change this to the right port - /dev/tty* on Linux and Mac and COM* on Windows
PORT = '/dev/ttyUSB0' # 指定通訊埠名稱

UNPACK_PAT = '<ccHHHcc'
ser_sds011 =  serial.Serial(PORT, 9600, bytesize=8, parity='N', stopbits=1)


def main():
    while True:
        data = ser_sds011.read(10)
        unpacked = struct.unpack(UNPACK_PAT, data)
        ts = datetime.now()
        pm25 = unpacked[2] / 10.0
        pm10 = unpacked[3] / 10.0
        
        print("{} , PM2.5: {}, PM10: {}".format(ts, pm25, pm10))
        db.insert_data( pm25, pm10)
        time.sleep(1)
    
    
if __name__ == '__main__':
    while True:
        try:
            main()
        except KeyboardInterrupt:
            print('KeyboardInterrupt')
            break
        except Exception as e:
            print(e)