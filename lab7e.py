#!/usr/bin/env python3
# Student ID: bjpatel18

class Time:
    def __init__(self, hour=12, minute=0, second=0):
        self.hour = hour
        self.minute = minute
        self.second = second

    def __str__(self):
        return f"{self.hour:02d}:{self.minute:02d}:{self.second:02d}"

    def __repr__(self):
        return f"{self.hour:02d}.{self.minute:02d}.{self.second:02d}"

    def format_time(self):
        return f"{self.hour:02d}:{self.minute:02d}:{self.second:02d}"

    def time_to_sec(self):
        minutes = self.hour * 60 + self.minute
        return minutes * 60 + self.second

    def change_time(self, seconds):
        nt = sec_to_time(self.time_to_sec() + seconds)
        self.hour, self.minute, self.second = nt.hour, nt.minute, nt.second

    def sum_times(self, t2):
        total = self.time_to_sec() + t2.time_to_sec()
        return sec_to_time(total)

def sec_to_time(seconds):
    t = Time()
    minutes, t.second = divmod(seconds, 60)
    t.hour, t.minute = divmod(minutes, 60)
    return t
