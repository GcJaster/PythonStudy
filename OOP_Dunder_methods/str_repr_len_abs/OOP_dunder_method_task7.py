from typing import NoReturn
import time


class Clock:
    def __init__(self, hours: int, minutes: int, seconds: int) -> NoReturn:
        self.hours = hours
        self.minutes = minutes
        self.seconds = seconds

    def get_time(self) -> int:
        return self.hours * 3600 + self.minutes * 60 + self.seconds


class DeltaClock:
    def __init__(self, clock1: Clock, clock2: Clock) -> NoReturn:
        self.clock1 = clock1
        self.clock2 = clock2

    def __str__(self) -> str:
        return time.strftime("%H: %M: %S", time.gmtime(len(self)))

    def __len__(self) -> int:
        diff = self.clock1.get_time() - self.clock2.get_time()
        if diff > 0:
            return diff
        return 0


def main():
    dt = DeltaClock(Clock(0, 0, 0), Clock(0, 0, 0))
    print(dt) # 01: 30: 00
    len_dt = len(dt) # 5400
    print(len_dt)


if __name__ == '__main__':
    main()