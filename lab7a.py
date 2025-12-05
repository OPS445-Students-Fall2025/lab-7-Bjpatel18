#!/usr/bin/env python3
# Student Id: Bjpatel18

class Time:
    """Simple object type for time of the day."""
    def __init__(self, hour=12, minute=0, second=0):
        self.hour = hour
        self.minute = minute
        self.second = second

def format_time(t):
    return f"{t.hour:02d}:{t.minute:02d}:{t.second:02d}"

def sum_times(t1, t2):
    sum_time = Time(0, 0, 0)
    sum_time.hour = t1.hour + t2.hour
    sum_time.minute = t1.minute + t2.minute
    sum_time.second = t1.second + t2.second

    # Carry seconds → minutes
    while sum_time.second >= 60:
        sum_time.second -= 60
        sum_time.minute += 1

    # Carry minutes → hours
    while sum_time.minute >= 60:
        sum_time.minute -= 60
        sum_time.hour += 1

    return sum_time

def valid_time(t):
    if t.hour < 0 or t.minute < 0 or t.second < 0:
        return False
    if t.minute >= 60 or t.second >= 60 or t.hour >= 24:
        return False
    return True

