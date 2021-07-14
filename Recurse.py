def factorical(x):
    '''This is a recursive function
    to find the factorical of an integer'''
    if x == 1:
        return 1
    else:
        return (x * factorical(x-1))

num = 5
print(f'factorical({num}) is: ',factorical(num))