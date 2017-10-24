print("Hello world!!!")
import os
import pandas


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



def noName():
    SimDates = readSimDir(SIM_DIR)
    for simDate in SimDates:
        print('--')
        for zoneNum in range(1,LAST_ZONE):
            zoneName = os.path.join(simDate, 'zone'+str(zoneNum)+'.txt')
            print(zoneName)






noName()