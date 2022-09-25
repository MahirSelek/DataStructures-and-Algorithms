# Python code for implementation of Insertion Sort Algorithm

# Define a function to do insertion sort
def insertion(arr):

    # Loop 1 to len(arr)
    # Since we consider the number at index 0 to be sequential, 
    # our loop should start from the first index.
    for i in range(1,len(arr)):  

        key = arr[i]

        # Move elements of arr[0..i-1], that are
        # greater than key, to one position ahead
        # of their current position
        j = i-1
        while j >=0 and key < arr[j] :
                arr[j+1] = arr[j]
                j -= 1
        arr[j+1] = key



random_series = [1,435,6,234,2,-34]
insertion(random_series)
print(random_series)

