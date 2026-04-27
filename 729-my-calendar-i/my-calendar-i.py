class MyCalendar:

    def __init__(self):
        self.calendar = []
    def book(self, start: int, end: int) -> bool:
        index = bisect.bisect_left(self.calendar, [start, end])
        if index < len(self.calendar) and self.calendar[index][0] < end:
            return False
        if index > 0 and self.calendar[index-1][1] > start:
            return False
        self.calendar.insert(index, [start, end])
        return True

# Your MyCalendar object will be instantiated and called as such:
# obj = MyCalendar()
# param_1 = obj.book(startTime,endTime)