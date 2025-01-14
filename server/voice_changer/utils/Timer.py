import time
import inspect


class Timer(object):
    storedSecs = {}  # Class variable

    def __init__(self, title: str, enalbe: bool = True):
        self.title = title
        self.enable = enalbe
        self.secs = 0
        self.msecs = 0
        self.avrSecs = 0

        if self.enable is False:
            return

        self.maxStores = 10

        current_frame = inspect.currentframe()
        caller_frame = inspect.getouterframes(current_frame, 2)
        frame = caller_frame[1]
        filename = frame.filename
        line_number = frame.lineno
        self.key = f"{title}_{filename}_{line_number}"
        if self.key not in self.storedSecs:
            self.storedSecs[self.key] = []

    def __enter__(self):
        if self.enable is False:
            return
        self.start = time.time()
        return self

    def __exit__(self, *_):
        if self.enable is False:
            return
        self.end = time.time()
        self.secs = self.end - self.start
        self.msecs = self.secs * 1000  # millisecs
        self.storedSecs[self.key].append(self.secs)
        self.storedSecs[self.key] = self.storedSecs[self.key][-self.maxStores:]
        self.avrSecs = sum(self.storedSecs[self.key]) / len(self.storedSecs[self.key])
