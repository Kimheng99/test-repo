import matplotlib.pyplot
import numpy



class make:
    def __init__(self,week1, week2, week3):
        self.week1 = week1
        self.week2 = week2
        self.week3 = week3
    def ouput(self):
        print("Week1: ",self.week1)
        print("Week2: ",self.week2)
        print("Week3: ",self.week3)

        data = ["Week1", "Weeek2", "Week3"]
        value = numpy.array([self.week1, self.week2, self.week3])
        matplotlib.pyplot.bar(data,value)
        matplotlib.pyplot.show()
