def insertion_sort(array):
    for item in range(1, len(array)):
        value_to_sort = array[item]
        while item > 0 and array[item] < array[item-1]:
            array[item] , array[item-1] = array[item-1], array[item]
            item = item - 1
    return array
