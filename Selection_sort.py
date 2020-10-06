# Time:  O(N^2)   ,   Space:  O(1)

def selection_sort(array):
    for i in range(0 , len(array)-1):
        min_value = i
        
        for j in range(i+1, len(array)):
            if array[j] < array[min_value]:
                min_value = j
                array[min_value] , array[i] = array[i], array[min_value]
    return array





print(selection_sort([6,7,8,7,6,1,2,1,10,5,4,5,6,7,6,7,0]))
