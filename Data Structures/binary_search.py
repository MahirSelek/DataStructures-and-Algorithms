#Iterative implementation of binary search in Python

my_list = [2,3,32,34,2334,23433,55555]
elem = 2

def binary_search(my_list, elem):

    first_index = 0
    last_index = len(my_list) - 1

    while first_index <= last_index:
        i = (first_index + last_index) / 2
        if my_list[i] == elem:
            return "found at position".format(elem=elem, i=i)
        elif my_list[i] > elem:
            last_index = i-1
        elif my_list[i] < elem:
            first_index = i+1
        else:
            return "not found in the list" .format(elem=elem)

binary_search(my_list,elem)