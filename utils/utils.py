import time
import random

def arrayGenerator(size: int, maxInt: int = 100):
    return [random.randint(0, maxInt) for _ in range(size)]

def printTitle(title: str):
    print('\n\n'+ ("-" * len(title)))
    print(title)

def printArray(dataArray, sorted: bool = False):
    if sorted:
        print("\nSorted Array")
    else:
        print("\nUnsorted Array")
    for value in dataArray:
        print(str(value), end=' ')

class Timer:
    lastTime = 0
    def __init__(self):
        self.lastTime = 0
        self.startTime = 0
    def setTimer(self):
        self.startTime = time.time_ns()
    def getTimer(self):
        self.lastTime = time.time_ns() - self.startTime
        print(f'\n-- TIMER : {self.lastTime}ns --')
        return self.lastTime
    def getTimerFunctionExecution(self, func, *params):
        self.setTimer()
        value = func(*params)
        self.getTimer()
        return value