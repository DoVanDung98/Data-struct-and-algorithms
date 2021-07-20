# Selection Sort
'''
    1. Set the first element as minimum
    2. Compare minimum with second element. If the second element is smaller than
    minimum, assign the second element as minimum
    
    Compare minimum with the third element. Again, if the third element is smaller,
    then assign minimum to the third element otherwise do nothing. The process goes
    on until the last element
    3. After each iteration, minimum is placed in the front of the unsorted list.
    4. For each iteration, indexing starts from the first unsorted element. Step 1 to 3
    are repeated until all the elements are placed at their correct poisitions. 
'''
# Selection sort in Python
def SelectionSort(array, size):
    for step in range(size):          
        min_idx = step
        for i in range(step+1, size):
            if array [min_idx]> array[i]:
                min_idx = i
        (array[min_idx], array[step]) = (array[step], array[min_idx])

array = [-4,22,5,6,1]
size = len(array)
SelectionSort(array, size)
print(array)