"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        intervals.sort(key=lambda x: x.start)
        if intervals:
            contain = [intervals[0]]
        

        for i in range(1, len(intervals)):
            if contain[-1].end > intervals[i].start:
                return False
            contain.append(intervals[i])
        return True