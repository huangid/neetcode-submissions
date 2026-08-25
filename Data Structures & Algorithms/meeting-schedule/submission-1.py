"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        prev = 0
        interval = []
        for i in range(len(intervals)):
            interval.append([intervals[i].start, intervals[i].end])
        interval.sort()
        for inter in interval:
            start, end = inter
            if start < prev:
                return False
            prev = end
        return True