class Solution:
    def __init__(self, n) -> None:
        self.N = n
        a, b, c, d = 2,4,8,15 # base values when m = 4
        # above numbers can be easily calculated by following below steps
        # when m = 4, n = 1, ways would be 2^1 = 2
        # when m = 4, n = 2, ways would be 2^2 = 4
        # when m = 4, n = 3, ways would be 2^3 = 8
        # when m = 4, n = 4, ways would be 2^4 - 1 = 15 # -1 because we cannot miss 4 or more consecutive classes
        # so when m == n then ways would be 2^m - 1
        # this solution can be easily extended to any m
        # after finding out m base values we can use below formula to find out ways for any n
        for i in range(4, self.N):
            a, b, c, d = b, c, d, a+b+c+d
        self.ways_to_attend_classes = d
        self.ways_to_miss_ceremony = d - c

    def get_ways_to_attend_classes(self):
        return self.ways_to_attend_classes
    
    def get_ways_to_miss_ceremony(self):
        return self.ways_to_miss_ceremony
    