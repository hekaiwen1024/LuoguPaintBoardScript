import os
from scipy import ndimage
import re
import time
import json
import requests
import threading
import queue

color = 
{
    '(0, 0, 0)': '0',
    '(255, 255, 255)': '1',
    '(170, 170, 170)': '2',
    '(85, 85, 85)': '3',
    '(254, 211, 199)': '4',
    '(255, 196, 206)': '5',
    '(250, 172, 142)': '6',
    '(255, 139, 131)': '7',
    '(244, 67, 54)': '8',
    '(233, 30, 99)': '9',
    '(226, 102, 158)': 'a',
    '(156, 39, 176)': 'b',
    '(103, 58, 183)': 'c',
    '(63, 81, 181)': 'd',
    '(0, 70, 112)': 'e',
    '(5, 113, 151)': 'f',
    '(33, 150, 243)': 'g',
    '(0, 188, 212)': 'h',
    '(59, 229, 219)': 'i',
    '(151, 253, 220)': 'j',
    '(22, 115, 0)': 'k',
    '(55, 169, 60)': 'l',
    '(137, 230, 66)': 'm',
    '(215, 255, 7)': 'n',
    '(255, 246, 209)': 'o',
    '(248, 203, 140)': 'p',
    '(255, 235, 59)': 'q',
    '(255, 193, 7)': 'r',
    '(255, 152, 0)': 's',
    '(255, 87, 34)': 't',
    '(184, 63, 39)': 'u',
    '(121, 85, 72)': 'v'
}

# Get gif map info
im_array = ndimage.imread("earthman.bmp", mode="RGB")
len_row = len(im_array)
len_col = len(im_array[0])

print(len_row, len_col)

# cookies 
mycookies = {
    'UM_distinctid': '160a5a02f1e34c-00a286642c06828-173a7640-e1000-160a5a02f1f5c8',
    '__client_id': '236f31d4e24a406d3dba65cce3ec5f24da66437a',
    'CNZZDATA5476811': 'cnzz_eid%3D322944717-1514602952-%26ntime%3D1514602952'
}


# 基础绘画基准
base_row, base_col = 200, 600

mydata = {
    'x': 0,
    'y': 1,
    'color': '5'
}

s = requests.Session()
rr = s.post('https://www.luogu.org/paintBoard/paint', data = mydata, cookies = mycookies)
print(rr.text)

def main():
    for
    
if __name__ == "__main__":
    main()
