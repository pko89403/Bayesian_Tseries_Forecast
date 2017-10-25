print("Hello world!!!")
import os
from pandas import DataFrame
import numpy as np

LAST_ZONE=13
SIM_DIR='./Simulation/'
TIME_CNT=37

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
    line = list(map(int,line))
    f.close()
    return line

def makeDframe(zoneList):
    df = DataFrame(index=range(1,TIME_CNT+1))
    i=0
    for zone in zoneList:
        r_tmp = readSimFile(zone)
        zone = 'zone'+ str(i+1)
        df.insert(column=zone, value=r_tmp, loc=(i) )
        i = i + 1
    return df


def read_RawData():
    simData = {}
    SimDates = readSimDir(SIM_DIR)  # SimDates is Simulation date list

    for simDate in SimDates:
        zoneList = []

        for zoneNum in range(1,LAST_ZONE): # make zone list 1 to 12. zoneList is a list that contains path of the zone1.txt to zone12.txt
            zoneName = os.path.join(simDate, 'zone'+str(zoneNum)+'.txt')
            zoneList.append(zoneName)

        dateDframe = makeDframe(zoneList)

        simDate = simDate.split('/')[-1]
        simData[simDate]=dateDframe
    return simData

raw_Data = read_RawData()
raw_Data_Keys = list(raw_Data.keys())
print(raw_Data_Keys[1])
print(raw_Data[raw_Data_Keys[1]])

