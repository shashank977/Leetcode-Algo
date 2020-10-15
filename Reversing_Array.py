def reverse(array):
    start = 0
    end = len(array)-1
    
    while start < end:
        array[start], array[end] = array[end], array[start]
        start+=1
        end-=1
    return array

print(reverse([1,2,3,4,5,6,7,8,9,10,2,4,6,8,9,7,3,5,3,3212,4,66,7,8,8,8,6]))
