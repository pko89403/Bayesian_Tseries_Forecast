import readRawData
import numpy as np
import tensorflow as tf

read_Raw = readRawData.SimulationData()
raw_Data = read_Raw.read_RawData()
raw_Data_Keys = list(raw_Data.keys() )
timeCnt = read_Raw.timeCnt

class TrainingData:
    trainX = []
    trainY = []

    def __init__(self):
        trainX = []
        trainY = []
        for rawDataKey in raw_Data_Keys:
            rawData = raw_Data[rawDataKey]

            rd2MX = rawData.as_matrix()

            for i in range(timeCnt - 1):
                tmp_X = rd2MX[i]
                tmp_Y = rd2MX[i + 1]
                trainX.append(tmp_X)
                trainY.append(tmp_Y)

        trainX = np.float32(trainX)
        trainY = np.float32(trainY)
        self.trainX = trainX
        self.trainY = trainY

    def getX(self):
        return self.trainX

    def getY(self):
        return self.trainY

    def getSelectedX(self, xList):
        return self.trainX[:,xList]

    def getSelectedY(self, yList):
        return self.trainY[:,yList]
