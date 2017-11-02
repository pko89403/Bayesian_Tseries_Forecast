from trainData import TrainingData
import tensorflow as tf

trainData = TrainingData()

zoneUsed = [0,1,2,3,4,5,6,7,8,9,10,11]

trainX = trainData.getSelectedX(zoneUsed)
trainX = tf.transpose(trainX)
trainY = trainData.getY()
trainY = tf.transpose(trainY)

W = tf.Variable(tf.random_uniform( [1,len(zoneUsed)] , -1.0 , 1.0))
b  = tf.Variable(tf.random_uniform([1], -1.0, 1.0))


hypothesis = tf.matmul(W,trainX) + b



for zone in zoneUsed:
    cost = tf.reduce_mean(tf.square(hypothesis- trainY[zone]))
    learnRate = tf.Variable(0.000001)
    optimizer = tf.train.GradientDescentOptimizer(learnRate)
    train = optimizer.minimize(cost)

    init = tf.global_variables_initializer()
    saver = tf.train.Saver()

    sess = tf.Session()
    sess.run(init)

    for step in range(10000):
        sess.run(train)
        if(step % 100 == 0):
            save_path = saver.save(sess, './model'+str(zone+1)+'.ckpt')
            print(step,sess.run(cost),sess.run(W))
    sess.close()
