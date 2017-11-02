print("Hello world!!!")
import os
from pandas import DataFrame

class SimulationData:
    dir ='./Simulation/'
    zoneCnt = 13
    timeCnt = 37

    def __init__(self, dir='./Simulation/', zoneCnt=13, timeCnt=37):
        self.dir = dir
        self.zoneCnt = zoneCnt
        self.timeCnt = timeCnt

    def __del__(self):
        print('terminate')

    def readSimDir(self):
        dirName = self.dir
        list = []
        fileNames = os.listdir(dirName)

        for fileName in fileNames:
            full_File_Name = os.path.join(dirName, fileName)
            list.append(full_File_Name)

        return list

    def readSimFile(self, fileName):
        f = open(fileName, 'r')
        line = f.readlines()
        line = list(map(int, line))
        f.close()
        return line

    def makeDframe(self, zoneList):
        df = DataFrame(index=range(1, self.timeCnt + 1))
        i = 0
        for zone in zoneList:
            r_tmp = self.readSimFile(zone)
            zone = 'zone' + str(i + 1)
            df.insert(column=zone, value=r_tmp, loc=(i))
            i = i + 1
        return df

    def read_RawData(self):
        simData = {}
        SimDates = self.readSimDir()  # SimDates is Simulation date list

        for simDate in SimDates:
            zoneList = []

            for zoneNum in range(1,
                                 self.zoneCnt):  # make zone list 1 to 12. zoneList is a list that contains path of the zone1.txt to zone12.txt
                zoneName = os.path.join(simDate, 'zone' + str(zoneNum) + '.txt')
                zoneList.append(zoneName)

            dateDframe = self.makeDframe(zoneList)

            simDate = simDate.split('/')[-1]
            simData[simDate] = dateDframe  # simData structure is dictionary [date, per zone population dataFrame]
        return simData




