class Solution:
    def minimumBoxes(apple, capacity) -> int:
        total_apple=sum(apple)#adding apples
        capacity.sort(key=lambda b:-b)# sorting in reverse order
        num_boxes=0
        for bix in capacity:
            total_apple-=bix
            num_boxes+=1
            if total_apple<=0:#it should stop when it reaches 0
                break
        return num_boxes
    apple=[1,2,3]
    capacity=[5,8,1]
    print(minimumBoxes(apple,capacity))