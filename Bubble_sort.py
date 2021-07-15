# Bubble Sort
'''
    1. Starting from fist index, compare the first and the second elements
    2. If the first element is greater than second element, they are swapped
    3. Now, compare the second and third element. Swap them if they are not in order.
    4. The above process goese on until the last element
'''
import time

def Bubble_Sort(array):
    for i in range(len(array)):
        for j in range(len(array)):
            temp = 0
            if array[i] > array[j]:
                temp = array[j]
                array[j] = array[i]
                array[i] = temp           
    return array

print(Bubble_Sort([-2, 45, 0, 11, -9]))


# Optimized Bubble sort in Python
# import time
# def bubbleSort(array):
#     start = time.time()
#     # loop through each element of array
#     for i in range(len(array)):
            
#         # keep track of swapping
#         swapped = False
        
#         # loop to compare array elements
#         for j in range(0, len(array) - i - 1):

#             # compare two adjacent elements
#             # change > to < to sort in descending order
#             if array[j] > array[j + 1]:

#                 # swapping occurs if elements
#                 # are not in the intended order
#                 temp = array[j]
#                 array[j] = array[j+1]
#                 array[j+1] = temp

#                 swapped = True
                
#         # no swapping means the array is already sorted
#         # so no need for further comparison
#         if not swapped:
#             break
#     end = time.time()
#     print("Times excute: ", (end-start))
    

# data = [-2, 45, 0, 11, -9]

# bubbleSort(data)

# print('Sorted Array in Ascending Order:')
# print(data)