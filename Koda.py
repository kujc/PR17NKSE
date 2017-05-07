
import csv

import numpy as np
import matplotlib.pyplot as plt
from datetime import datetime
from scipy.stats import multivariate_normal as mvn
from scipy.stats import beta

from csv import DictReader
import pandas as pa

def fileReaderSmucNesrece():
    fp = open("evidencanesrecnasmuciscihV1.csv", "rt", encoding=" utf -8 ")
    reader = DictReader(fp)
    return [line for line in reader]



SmucNes = fileReaderSmucNesrece()

SmucNes = pa.DataFrame(SmucNes)
titles = []
for i in SmucNes:
    titles.append(i)
def tf(t):
    st = 0
    for i in SmucNes[t]:
        if i == 'Da':
            SmucNes.set_value(st, t, "True")
        elif i == "Ne":
            SmucNes.set_value(st, t, "False")
        else:
            SmucNes.set_value(st, t, "")
        st += 1
def tfmake():
    num = [3, 4, 5, 13, 14, 15]
    for i in num:
        tf(titles[i])
    num2 = [9, 16, 17, 19, 20 ]
    for i in num2:
        udA(titles[i])
def udA(t):
    dic = {}
    temp=[]
    st = 0
    for i in SmucNes[t]:
        if len(i)>0:
            temp = i.split(" ", 1)
            if temp[0] not in dic:
                if temp[0] == 25:
                    dic[25] = 'ostalo'
                elif temp[0] == 'NOÈNA':
                    dic[7] = 'NOÈNA'
                else:
                    if len(temp) > 1:
                        dic[temp[0]] = temp[1]

            if temp[0].isdigit():
                SmucNes.set_value(st, t, temp[0])
            else:
                for i in dic:
                    if temp[0] == dic[i]:
                        SmucNes.set_value(st, t, i)
                SmucNes.set_value(st, t, "")
        else:
            SmucNes.set_value(st, t, "")

        st += 1


tfmake()
print(SmucNes)
