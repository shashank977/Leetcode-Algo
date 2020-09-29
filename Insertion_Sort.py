#  Time:  O(N^2)   ,   Space:  O(1)

#  (1)
def insertion_sort(array):
    for item in range(1, len(array)):
        value_to_sort = array[item]
        while item > 0 and array[item] < array[item-1]:
            array[item] , array[item-1] = array[item-1], array[item]
            item = item - 1
    return array                       




# (2) Using Swap function
def insertion_sort(array):
    for i in range(1, len(array)):
        j = i
        while j > 0 and array[j] < array[j-1]:
            swap(j, j-1, array)
            j -= 1
    return array

def swap(i, j, array):
    array[i], array[j] = array[j], array[i]
