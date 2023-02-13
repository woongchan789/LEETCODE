class Solution(object):
    def findPoisonedDuration(self, timeSeries, duration):
        poisoned_time = 0
        for i in range(len(timeSeries)-1):
            if timeSeries[i] + duration <= timeSeries[i+1]:
                poisoned_time += duration
            else:
                poisoned_time += timeSeries[i+1] - timeSeries[i]
        poisoned_time += duration
        return poisoned_time