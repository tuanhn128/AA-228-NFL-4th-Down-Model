import numpy as np
import csv


# Implementation of QLearning which takes in a datatset csv with s, a, r, s' columns.
# Learns a Q* and stores it in self.Q.
class QLearning:
    def __init__(self, dataset, numStates, numActions, learning_rate, discount):
        self.datasetArray = np.genfromtxt(dataset, delimiter=',', skip_header=1)
        self.numStates = numStates
        self.numActions = numActions
        self.Q = np.zeros((self.numStates, self.numActions))
        self.learning_rate = learning_rate
        self.discount = discount

    def update(self, s, a, r, sp, learning_rate):
        self.Q[s, a] += learning_rate * (r + self.Q[sp, :].max() * self.discount - self.Q[s, a])

    def learn(self):
        totalUpdates = self.datasetArray.shape[0]
        numUpdates = 0
        for row_num in range(self.datasetArray.shape[0]):
            row = self.datasetArray[row_num, :]
            self.update(int(row[0]), int(row[1]), int(row[2]), int(row[3]), self.learning_rate - (numUpdates * self.learning_rate)/totalUpdates)
            numUpdates += 1