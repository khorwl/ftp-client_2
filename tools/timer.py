import time
import threading


class Timer:
    def __init__(self):
        self._interval = 1 / 60
        self._thread = threading.Thread(target=self._thread_target, daemon=True)
        self._elapsed = 0
        self._thread.start()

    def _thread_target(self):
        while True:
            self._elapsed += self._interval
            time.sleep(self._interval)

    @property
    def elapsed(self):
        return self._elapsed
