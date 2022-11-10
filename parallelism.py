import csv
import threading
from time import *
from multiprocessing import Process, Pool
import numpy as np


def print_matrix(matrix):
    for i in matrix:
        print(*i, end='\n')


class Multiplication:

    def __init__(self, size1=None, size2=None):
        self.matrix1 = self.read_csvmatrix('matrix1.csv')
        self.matrix2 = self.read_csvmatrix('matrix2.csv')
        self.final = np.zeros((len(self.matrix1),len(self.matrix2[0])))
        self.multi()

    def read_csvmatrix(self, name_file):
        matrix = []
        with open(name_file, 'r', encoding='utf-8') as file:
            reader = csv.reader(file, delimiter=',')
            for i in reader:
                i = [int(j) for j in i]
                matrix.append(i)

        return matrix

    def multi(self):
        thread = []
        for i in range(self.final.shape[0]):
            for j in range(self.final.shape[1]):
                t = threading.Thread(target=self.element, args=[(i,j)])
                t.start()
                thread.append(t)

            for t in thread:
                t.join()

        print_matrix(self.final)

    def element(self, index):
        i, j = index
        for k in range(len(self.matrix2)):
            self.final[i][j] += self.matrix1[i][k] * self.matrix2[k][j]




task1 = Multiplication()

