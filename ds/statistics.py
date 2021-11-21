import math

def mean(*args):
    val_sum = sum(args)
    return val_sum / len(args)

def median(*args): # middle element among a list of elements
    if len(args) % 2 == 0: # if even number of elements in the list
        i = round((len(args) + 1) / 2) # if there are 4 elements, pick 3rd element
        j = i - 1 # then pick the 2nd element
        return (args[i] + args[j]) / 2
    else:
        k = round(len(args) / 2)
        return args[k]

def mode(*args): # element(s) that occurs more number of times in a sample
    # create a dictionary with key as each unique element and value as the number of occurences
    dict_vals = {i: args.count(i) for i in args}
    max_list = [k for k, v in dict_vals.items() if v == max(dict_vals.values())] # create a list of values from the dict for values are max
    return max_list # could be one value or many values

def variance(*args): # variance in a sample is ( (x(i) - mean(X)) ^ 2 ) / (n - 1)
    mean_val = mean(*args)
    numerator = 0
    for i in args:
        numerator += (i - mean_val) ** 2
    denominator = len(args) - 1
    return numerator/denominator

def standard_deviation(*args): # sqrt of variance
    return math.sqrt(variance(*args))

# coefficient of variation if a list of miles and kms of same distances are there
# then this will show that both the list have same coefficient of variation - indicating that both values are pointing
# to same quantity/feature
def coefficient_variation(*args):
    return standard_deviation(*args) / mean(*args)

# covariance
# to see if any two values (x and y) are moving in the same direction
#           Market cap (x)  Earnings (y)
#   Apple   1532            58
#   MS      1488            35
#   Amazon  1343            75
#   Google  928             41
#   FB      615             17
# Covariance (COV) = (sum of (x(i) - xbar) * (y(i) - ybar)) / (n - 1)
# COV > 0 : moving together
# COV < 0 : moving opposite
# COV = 0 : independent
def covariance(*args):
    #  args = [[1532, 1488, 1343, 928, 615], [58, 35, 75, 41, 17]]
    list_1 = [i[0] for i in args]
    list_2 = [i[1] for i in args]

    list_1_mean = mean(*list_1[0])
    list_2_mean = mean(*list_2[0])

    numerator = 0
    if len(list_1[0]) == len(list_2[0]):
        for i in range(len(list_1[0])):
            numerator += (list_1[0][i] - list_1_mean) * (list_2[0][i] - list_2_mean)
        denominator = len(list_1[0]) - 1
        return numerator/denominator
    else:
        print("Error")

# correlation coefficient
# adjusts covariance to see relationships properly
# r = (COV(X, Y))/ (SD(X) * SD(Y))
# -1 < r < 1
# 1 = perfect correlation
# closer to 1 = close relation to values
# negative r = inverse
# 0 means they are independent
def correlation_coefficient(*args):
    #  args = [[1532, 1488, 1343, 928, 615], [58, 35, 75, 41, 17]]
    list_1 = [i[0] for i in args]
    list_2 = [i[1] for i in args]

    list_1_sd = standard_deviation(*list_1[0])
    list_2_sd = standard_deviation(*list_2[0])

    denominator = list_1_sd * list_2_sd
    numerator = covariance(*args)

    return numerator / denominator


print(f"Mean : {mean(1, 3, 5, 7, 9, 11)}")
print(f"Median : {median(1, 3, 5, 7, 9)}")
print(f"Median : {median(1, 2, 3, 4, 5, 6)}")

print(f"Mode : {mode(1, 2, 4, 4, 5, 5, 6, 6)}") # 4, 5 and 6
print(f"Mode : {mode(1, 2, 4, 5, 6)}") # all of them

print(f"Variance : {variance(4, 6, 3, 5, 2)}")
print(f"Standard Deviation : {standard_deviation(4, 6, 3, 5, 2)}")

print(f"CV (miles) : {coefficient_variation(3, 4, 4.5, 3.5)}")
print(f"CV (kms) : {coefficient_variation(4.828, 6.437, 7.242, 5.632)}")

m_d_list = [[1532, 1488, 1343, 928, 615], [58, 35, 75, 41, 17]]
print(f"Stock Covariance : {covariance(m_d_list)}")
print(f"Correlation Coefficient : {correlation_coefficient(m_d_list)}")