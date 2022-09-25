# Python code for implementation of Selection Sort Algorithm

# Define a function to do selection sort
def selection(arr):

    # Traverse through all array elements
    for i in range(len(arr)):
        min_index = i

        # Find the minimum element in remaining 
        # unsorted array
        for j in range(i+1,len(arr)):
            if arr[min_index] > arr[j]:
                min_index = j

        # Swap the found minimum element with 
        # the first element
        if min_index != i:
            arr[min_index], arr[i] = arr[i], arr[min_index]


random_series = [1,435,6,234,2,-34]
selection(random_series)
print(random_series)