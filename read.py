print("Hello world!!!")
import os
from pandas import DataFrame as df
import numpy as np

LAST_ZONE=13
SIM_DIR='./Simulation/'





def readSimDir(dirName):
    list = []
    fileNames = os.listdir(dirName)

    for fileName in fileNames:
        full_File_Name = os.path.join(dirName, fileName)
        list.append(full_File_Name)

    return list

def readSimFile(fileName):
    f = open(fileName, 'r')
    line = f.readlines()
    print(line)
    f.close()

def makeDframe(zoneList):

    tmp = df(columns=('zone1','zone2','zone3','zone4','zone5','zone6','zone7','zone8','zone9','zone10','zone11','zone12'))



def noName():
    SimDates = readSimDir(SIM_DIR)
    for simDate in SimDates:
        print('--')
        zoneList = []
        for zoneNum in range(1,LAST_ZONE):
            zoneName = os.path.join(simDate, 'zone'+str(zoneNum)+'.txt')
            zoneList.append(zoneName)
        makeDframe(zoneList)





noName()