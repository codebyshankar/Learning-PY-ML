import math as mt

A = [73, 73, 76, 77, 81, 100]

sum = 0
for a in A:
    sum += a

print("Sum of all ", sum)
average = sum/len(A)
print("Average is ", average)

stddev = 0.0
for a in A:
    stddev += mt.pow((a - average), 2)

stddev = stddev/len(A)
stddev = mt.sqrt((stddev))
print("Standard Deviation is ", stddev)