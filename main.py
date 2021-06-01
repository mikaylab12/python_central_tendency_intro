import numpy
from scipy import stats
marks = [90, 72, 82, 90, 69, 19, 23, 30, 45, 5]
# calculating mean
my_mean = numpy.mean(marks)
print("The mean of marks is ", my_mean)
# calculating median
my_median = numpy.median(marks)
print("The median of marks is ", my_median)
# calculating mode
my_mode = stats.mode(marks)
print("The mode of marks is ", my_mode)
# calculating range
my_range = numpy.ptp(marks)
print("The range of marks is ", my_range)
# calculating 25th / 1st quartile
my_quartile = numpy.percentile(marks, 25)
print("The 25% percentile of marks is ", my_quartile)
# calculating 75th / 3rd quartile
my_quartile = numpy.percentile(marks, 75)
print("The 75% percentile of marks is ", my_quartile)
# calculating variance
x = numpy.var(marks)
print("The variance of marks is ", x)
# calculating standard deviation
my_stdn = numpy.std(marks)
print("The standard deviation of marks is ", my_stdn)

