# Basic Two-Dimensional Array Arithmetic


## Dependencies
import numpy as np

## Data: yearly salary in ($1000) [2017, 2018, 2019]
alice = [99, 101, 103]
bob = [110, 108, 105]
tim = [90, 88, 85]
salaries = np.array([alice, bob, tim])
taxation = np.array([[0.2, 0.25, 0.22],
                     [0.4, 0.5, 0.5],
                     [0.1, 0.2, 0.1]])

## One-liner
max_income = np.max(salaries - salaries * taxation)

## Result
print(max_income)
'''
81.0
'''



# Working with NumPy Arrays: Slicing, Broadcasting, and Array Types


## Dependencies
import numpy as np

## Data: yearly salary in ($1000) [2025, 2026, 2027]
dataScientist = [130, 132, 137]
productManager = [127, 140, 145]
designer = [118, 118, 127]
softwareEngineer = [129, 131, 137]
employees = np.array([dataScientist,
                      productManager,
                      designer,
                      softwareEngineer])

## One-liner
employees[0, ::2] = employees[0, ::2] * 1.1

## Result
print(employees)
'''
[[143 132 150]
 [127 140 145]
 [118 118 127]
 [129 131 137]]
'''



# Conditional Array Search, Filtering, and Broadcasting to Detect Outliers


## Dependencies
import numpy as np

## Data: air quality index AQI data (row = city)
X = np.array(
    [[42, 40, 41, 43, 44, 43],  # Hong Kong
     [30, 31, 29, 29, 29, 30],  # New York
     [8, 13, 31, 11, 11, 9],  # Berlin
     [11, 11, 12, 13, 11, 12]])  # Montreal
cities = np.array(["Hong Kong", "New York", "Berlin", "Montreal"])

## One-liner
polluted = set(cities[np.nonzero(X > np.average(X))[0]])

## Result
print(polluted)
'''
{'Berlin', 'Hong Kong', 'New York'}
'''



# Boolean Indexing to Filter Two-Dimensional Arrays


## Dependencies
import numpy as np

## Data: popular Instagram accounts (millions followers)
inst = np.array([[232, "@instagram"],
                 [133, "@selenagomez"],
                 [59, "@victoriassecret"],
                 [120, "@cristiano"],
                 [111, "@beyonce"],
                 [76, "@nike"]])

## One-liner
superstars = inst[inst[:, 0].astype(float) > 100, 1]

## Results
print(superstars)
'''
['@instagram' '@selenagomez' '@cristiano' '@beyonce']
'''




# Broadcasting, Slice Assignment, and Reshaping to Clean Every i-th Array Element


## Dependencies
import numpy as np

## Sensor data (Mo, Tu, We, Th, Fr, Sa, Su)
tmp = np.array([1, 2, 3, 4, 3, 4, 4,
                5, 3, 3, 4, 3, 4, 6,
                6, 5, 5, 5, 4, 5, 5])

## One-liner
tmp[6::7] = np.average(tmp.reshape((-1, 7)), axis=1)

## Result
print(tmp)
'''
[1 2 3 4 3 4 3 5 3 3 4 3 4 4 6 5 5 5 4 5 5]
'''



# When to Use the sort() Function and When to Use the argsort() Function in NumPy


## Dependencies
import numpy as np

## Data: SAT scores for different students
sat_scores = np.array([1100, 1256, 1543,
                       1043, 989, 1412, 1343])
students = np.array(["John", "Bob", "Alice",
                     "Joe", "Jane", "Frank", "Carl"])

## One-liner
top_3 = students[np.argsort(sat_scores)][:-4:-1]

## Result
print(top_3)
'''
['Alice' 'Frank' 'Carl']
'''




# How to Use Lambda Functions and Boolean Indexing to Filter Arrays


## Dependencies
import numpy as np

## Data (row = [title, rating])
books = np.array([['Coffee Break NumPy', 4.6],
                  ['Lord of the Rings', 5.0],
                  ['Harry Potter', 4.3],
                  ['Winnie-the-Pooh', 3.9],
                  ['The Clown of God', 2.2],
                  ['Coffee Break Python', 4.7]])

## One-liner
predict_bestseller = lambda x, y: x[x[:, 1].astype(float) > y]

## Results
print(predict_bestseller(books, 3.9))
'''
[['Coffee Break NumPy' '4.6']
 ['Lord of the Rings' '5.0']
 ['Harry Potter' '4.3']
 ['Coffee Break Python' '4.7']]
'''



# How to Create Advanced Array Filters with Statistics, Math, and Logic


## Dependencies
import numpy as np

## Website analytics data:
## (row = day), (col = users, bounce, duration)
a = np.array([[815, 70, 115],
              [767, 80, 50],
              [912, 74, 77],
              [554, 88, 70],
              [1008, 65, 128]])
mean, stdev = np.mean(a, axis=0), np.std(a, axis=0)
# [811.2 76.4 88. ], [152.97764543 6.85857128 29.04479299]

## One-liner
outliers = ((np.abs(a[:, 0] - mean[0]) > stdev[0])
            * (np.abs(a[:, 1] - mean[1]) > stdev[1])
            * (np.abs(a[:, 2] - mean[2]) > stdev[2]))

## Result
print(a[outliers])
'''
[[1008   65  128]]
'''



# Simple Association Analysis: People Who Bought X Also Bought Y


## Dependencies
import numpy as np

## Data: row is customer shopping basket
## row = [course 1, course 2, ebook 1, ebook 2]
## value 1 indicates that an item was bought.
basket = np.array([[0, 1, 1, 0],
                   [0, 0, 0, 1],
                   [1, 1, 0, 0],
                   [0, 1, 1, 1],
                   [1, 1, 1, 0],
                   [0, 1, 1, 0],
                   [1, 1, 0, 1],
                   [1, 1, 1, 1]])

## One-liner
copurchases = np.sum(np.all(basket[:, 2:], axis=1)) / basket.shape[0]

## Result
print(copurchases)
'''
0.25
'''



# Intermediate Association Analysis to Find Bestseller Bundles


## Dependencies
import numpy as np

## Data: row is customer shopping basket
## row = [course 1, course 2, ebook 1, ebook 2]
## value 1 indicates that an item was bought.
basket = np.array([[0, 1, 1, 0],
                   [0, 0, 0, 1],
                   [1, 1, 0, 0],
                   [0, 1, 1, 1],
                   [1, 1, 1, 0],
                   [0, 1, 1, 0],
                   [1, 1, 0, 1],
                   [1, 1, 1, 1]])

## One-liner
copurchases = [(i, j, np.sum(basket[:, i] + basket[:, j] == 2)) for i in range(4) for j in range(i + 1, 4)]

## Result
print(max(copurchases, key=lambda x: x[2]))
'''
(1, 2, 5)
'''
