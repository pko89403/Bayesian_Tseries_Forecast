import readRawData
import numpy as np
import tensorflow as tf

read_Raw = readRawData.SimulationData()
raw_Data = read_Raw.read_RawData()
raw_Data_Keys = list(raw_Data.keys() )
timeCnt = read_Raw.timeCnt


def makeTrainData():

    global train_X, train_Y
    train_X = []
    train_Y = []
    for rawDataKey in raw_Data_Keys:
        rawData = raw_Data[rawDataKey]

        rd2MX = rawData.as_matrix()

        for i in range(timeCnt-1):
            tmp_X = rd2MX[i]
            tmp_Y = rd2MX[i + 1]
            train_X.append(tmp_X)
            train_Y.append(tmp_Y)

    train_X = np.float32(train_X)
    train_Y = np.float32(train_Y)

    return train_X, train_Y


