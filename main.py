from clases import *
from simular import *
from ordenar import *

from time import time
from numpy import arange
import matplotlib.pyplot as plt

bubbleList = []
mergeList = []
quickList = []
quickList2 = []


def generator(n):
    for i in n:
        vip = Lista()
        for _ in range(i):
            vip.adicionar(Persona(generarNombre(generarSexo()), generarEdad()))

        bubbleTime(vip.lista)
        mergeTime(vip.lista)
        quickTime(vip.lista)
        quickTime2(vip.lista)


def bubbleTime(x_list):
    initialTime = time()
    bubble_sort(x_list, "edad", True)
    finalTime = time()
    bubbleList.append(finalTime - initialTime)


def mergeTime(x_list):
    initialTime = time()
    merge_sort(x_list, "edad", True)
    finalTime = time()
    mergeList.append(finalTime - initialTime)


def quickTime(x_list):
    initialTime = time()
    quick_sort(x_list, 0, len(x_list) - 1)
    finalTime = time()
    quickList.append(finalTime - initialTime)


def quickTime2(x_list):
    initialTime = time()
    quick_sort_2(x_list, "edad", True)
    finalTime = time()
    quickList2.append(finalTime - initialTime)


# Run
if __name__ == "__main__":
    x = arange(0, 300, 3)
    generator(x)

    fig, ax = plt.subplots()
    bubbleLine, = plt.plot(x, bubbleList, '-r', label='BUBBLE')
    mergeLine, = plt.plot(x, mergeList, '-b', label='MERGE')
    quickLine, = plt.plot(x, quickList, '-g', label='QUICK')
    quickLine2, = plt.plot(x, quickList2, '-y', label='QUICK2')
    plt.xlabel('# DATA')
    plt.ylabel('TIME')
    leg = ax.legend()
    plt.show()
