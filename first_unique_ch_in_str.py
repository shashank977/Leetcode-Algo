# time: O(N)
# space: O(1)


def firstUniqChar(s):
        
        count= collections.Counter(s)
        
        for index,character in enumerate(s):
            if count[character]==1:
                return index
        
        return -1
