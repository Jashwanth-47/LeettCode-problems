from collections import Counter
class Solution:
    def uniqueOccurrences(arr) -> bool:
        counter=Counter(arr)
        s=set()
        for v in counter.values():
            if v in s:
                return False
            else:
                s.add(v)
        return True
    arr=[1,2,2,3,3,3]
    print(uniqueOccurrences(arr))