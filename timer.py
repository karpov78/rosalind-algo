import time, datetime

class Timer:
    def __enter__(self):
        self.start = time.perf_counter()
        return self

    def __exit__(self, *args):
        self.end = time.perf_counter()
        self.interval = self.end - self.start

    def __str__(self):
        return str(datetime.timedelta(milliseconds=int(self.interval * 1000)))
