# Using List Comprehension to Find Top Earners


## Data
employees = {'Alice': 100000,
             'Bob': 99817,
             'Carol': 122908,
             'Frank': 88123,
             'Eve': 93121}

## One-Liner
top_earners = [(k, v) for k, v in employees.items() if v >= 100000]

## Result
print(top_earners)
# [('Alice', 100000), ('Carol', 122908)]



# Using List Comprehension to Find Words with High Information Value


## Data
text = '''
Call me Ishmael. Some years ago - never mind how long precisely - having
little or no money in my purse, and nothing particular to interest me
on shore, I thought I would sail about a little and see the watery part
of the world. It is a way I have of driving off the spleen, and regulating
the circulation. - Moby Dick'''

## One-Liner
w = [[x for x in line.split() if len(x) > 3] for line in text.split('\n')]

## Result
print(w)
'''
[[], ['Call', 'Ishmael.', 'Some', 'years', 'never', 'mind', 'long', 'precisely', 'having'], 
['little', 'money', 'purse,', 'nothing', 'particular', 'interest'], 
['shore,', 'thought', 'would', 'sail', 'about', 'little', 'watery', 'part'], 
['world.', 'have', 'driving', 'spleen,', 'regulating'], ['circulation.', 'Moby', 'Dick']]
'''



# Reading a File

print([line.strip() for line in open("one_liner_03.py")])
# Output: <This file content>



# Using Lambda and Map Functions

## Data
txt = ['lambda functions are anonymous functions.',
       'anonymous functions dont have a name.',
       'functions are objects in Python.']

## One-Liner
mark = map(lambda s: (True, s) if 'anonymous' in s else (False, s), txt)

## Result
print(list(mark))
'''
[(True, 'lambda functions are anonymous functions.'),
(True, 'anonymous functions dont have a name.'),
(False, 'functions are objects in Python.')]
'''




# Using Slicing to Extract Matching Substring Environments

## Data
letters_amazon = '''
We spent several years building our own database engine,
Amazon Aurora, a fully-managed MySQL and PostgreSQL-compatible
service with the same or better durability and availability as
the commercial engines, but at one-tenth of the cost. We were
not surprised when this worked.
'''

## One-Liner
find = lambda x, q: x[x.find(q) - 18:x.find(q) + 18] if q in x else -1

## Result
print(find(letters_amazon, 'SQL'))
'''
a fully-managed MySQL and PostgreSQL
'''



# Combining List Comprehension and Slicing

## Data (daily stock prices ($))
price = [[9.9, 9.8, 9.8, 9.4, 9.5, 9.7],
         [9.5, 9.4, 9.4, 9.3, 9.2, 9.1],
         [8.4, 7.9, 7.9, 8.1, 8.0, 8.0],
         [7.1, 5.9, 4.8, 4.8, 4.7, 3.9]]

## One-Liner
sample = [line[::2] for line in price]

## Result
print(sample)
'''
[[9.9, 9.8, 9.5],
 [9.5, 9.4, 9.2],
 [8.4, 7.9, 8.0],
 [7.1, 4.8, 4.7]]
'''


# Using Slice Assignment to Correct Corrupted Lists


## Data
visitors = ['Firefox', 'corrupted', 'Chrome', 'corrupted',
            'Safari', 'corrupted', 'Safari', 'corrupted',
            'Chrome', 'corrupted', 'Firefox', 'corrupted']

## One-Liner
visitors[1::2] = visitors[::2]

## Result
print(visitors)
'''
['Firefox', 'Firefox', 'Chrome', 'Chrome', 'Safari', 'Safari',
'Safari', 'Safari', 'Chrome', 'Chrome', 'Firefox', 'Firefox']
'''



# Analyzing Cardiac Health Data with List Concatenation

## Dependencies
import matplotlib.pyplot as plt

## Data
cardiac_cycle = [62, 60, 62, 64, 68, 77, 80, 76, 71, 66, 61, 60, 62]

## One-Liner
expected_cycles = cardiac_cycle[1:-2] * 10

## Result
plt.plot(expected_cycles)
plt.show()



# Using Generator Expressions to Find Companies That Pay Below Minimum Wage

## Data
companies = {
    'CoolCompany': {'Alice': 33, 'Bob': 28, 'Frank': 29},
    'CheapCompany': {'Ann': 4, 'Lee': 9, 'Chrisi': 7},
    'SosoCompany': {'Esther': 38, 'Cole': 8, 'Paris': 18}
}

## One-Liner
illegal = [x for x in companies if any(y < 9 for y in companies[x].values())]

## Result
print(illegal)
'''
['CheapCompany', 'SosoCompany']
'''



# Formatting Databases with the zip() Function


## Data
column_names = ['name', 'salary', 'job']
db_rows = [('Alice', 180000, 'data scientist'),
           ('Bob', 99000, 'mid-level manager'),
           ('Frank', 87000, 'CEO')]

## One-Liner
db = [dict(zip(column_names, row)) for row in db_rows]

## Result
print(db)
'''
[{'name': 'Alice', 'salary': 180000, 'job': 'data scientist'},
 {'name': 'Bob', 'salary': 99000, 'job': 'mid-level manager'},
 {'name': 'Frank', 'salary': 87000, 'job': 'CEO'}]
'''


# Creating dictionary from 2 lists

## Data
keys = ['a', 'b', 'c']
values = [1, 2, 3]

## One-liner
d = dict(zip(keys, values))

## Result
print(d)
