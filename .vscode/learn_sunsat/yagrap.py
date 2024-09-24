# import matplotlib.pyplot
# import numpy


# name = ["week1", "week2", "week3", "week4", "week5"]
# data = numpy.array([100, 200, 300, 300, 250])

# matplotlib.pyplot.bar(name,data)
# matplotlib.pyplot.show()








import matplotlib.pyplot
import numpy

year = ["1994","2000" ,"2008", "2012" ]
#data = numpy.array([100,200,300,150])
data = [100,200,300,150]

matplotlib.pyplot.pie(data, labels=year)
matplotlib.pyplot.show()