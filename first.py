class MinStat:
    def __init__(self):
        self.values = [6,4,2,7]

    def add_num(self, num):
        self.values.append(num)
    def Min(self):
        min = self.values[0]
        for i in range(len(self.values)-1):
            if self.values[i]<min:
                min = self.values[i]
        return min

class MaxStat(MinStat):
    
    def Max(self):
        max = self.values[0]
        for i in range(len(self.values)-1):
            if self.values[i]>max:
                max = self.values[i]
        return max
    
class AverageStat(MinStat):
    def Average(self):
        average = sum(self.values)/len(self.values)
        return average

class Result(MaxStat, AverageStat):
    def Max(self):
        return max
    def Min(self):
        return min

minn = MinStat()
maxx = MaxStat()
aver = AverageStat()
print(minn.Min(),maxx.Max(), aver.Average() )

