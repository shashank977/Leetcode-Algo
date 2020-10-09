# Time:  O(N^2)   ,   Space:  O(1)
def bubble(array):
    isSorted=False

    while not isSorted:
        isSorted=True
        for i in range(0, len(array)-1):
            if array[i] > array[i+1]:
                array[i], array[i+1] = array[i+1], array[i]
                isSorted=False
    return array
