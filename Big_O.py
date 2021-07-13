# Caculation Big O
'''
    There are 5 steps:
        step1: Divide algorithms of your to action
        step2: caculation O from every action
        step3: Add Big O from every action
        step4: Cancel constants
        step5: Find the highest oder temrs
'''

# There are Big O function popular
'''
    Name                     Big-O
    constants                O(1)
    Logarit                  O(log(n))
    Linear                   O(n)
    Linear diary             O(n log(n))
    Level two                O(n^2)
    Block                    O(n^3)
    Index number             O(2^n)
'''

# Times Complexity
# 1. O(n)
'''
    Times constants: O(1)
        Times implement alogorithms don't depend on data size input
        Times complexity always Times complexity same always, whatever the input
'''

def get_data(data):
    return data
# print(get_data([1,3,4,5]))

# 2. Logarit: O(log(n))
'''
    The properties of algorithms there are logarit times complexity:
        Decreasing data size input in step
        No need all values
        Action continues will implement in several factors may have
    ex: binary search, binary tree...
'''

def binarySearch(listSorted, target):
    '''
        note: when implement binary search algorithms
        you need input list sorted
    '''
    left = 0
    right = len(listSorted) - 1
    while (left <= right):
        mid = (right+left)//2
        if (listSorted[mid] == target):
            return mid 
        elif (listSorted[mid]<target):
            left = mid + 1 
        else:
            right = mid - 1
    return -1
# print(binarySearch([1,2,3,4,33],33))

# 3. Linear Times Complexity O(n)
'''
    There are properties linear times complexity
        Number actions ratio linear with size(n)
        ex: implement manipulations in 100 times,
        each times to each element in list contains 100 element
    ex: copy, insert in a array, delete element in array, for loop
    algorithm: linear search
'''

def linearSearch(sortedList, target):
    for i in range(len(sortedList)):
        if (sortedList[i] == target):
            return i 
    return -1

# print(linearSearch([1,2,3,4,5],3))

# 4. Times complexity: (n log(n))
'''
    There properties of log(can call is standard) times complexity
        Each manipulation in data input has logarit times complexity
        ex: each value in data_1(O(n)) use search binary (Olog(n))
        search a value together in data_2
    
    There are algorithms has O(nlog(n)) times complexity:
        combine
        pile
        block
'''
def ListSorted(data_1):
    results = []
    results.append(binarySearch(data_2, values))

# 5. O(n^2)
'''
    There are of algorithm O(n^2):
        Implement caculation linear times for each in input 
        In list n folder, we implement n manipulations each folder.
        ex: 10 folder has 10^2 caculation
        ex: for ..:
                for ..
        Algorithms:
            Buble sort
            Insert sort
            Quick sort
            Selection sort
            Binary search
            Heap sort
'''
def search(list_1,x, y):
    for x in list_1:
        for y in list_1:
            return x,y

# 6. O(2^n)
'''
    There are properties of O(2^n) times complexity
        Increase douplicated each insert in dataset input
        ex: problem 'Tower of Hanoi'
        Algorithms:
            fibonacy recursive
'''
def fibonacy(num):
    if (num <=1):
        return num
    return fibonacy(num-1)+fibonacy(num-2)

# print(fibonacy(5))

# 7.O(n!)
'''
    There are properties times complexity factorial input size
    Fast grow up immediate small size input
    algorithms:
        heap map
'''
