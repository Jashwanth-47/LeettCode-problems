class Solution:
    def numberOfEmployeesWhoMetTarget(hours, target) -> int:
        n = 0
        for i in range(len(hours)):
            if hours[i] >= target:
                n += 1
        return n
    hours = [0,1,2,3,4]
    target = 2
    print(numberOfEmployeesWhoMetTarget(hours,target))