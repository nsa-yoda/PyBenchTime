from time import time

# Handle the running state of the timer
RUNNING = 1
PAUSED = 0
STOPPED = -1


def get_current_time():
    return time()


class Timer:
    def __init__(self):
        # Resets the timers, laps and summary
        self.state = STOPPED  # Maintains the state of the timer (RUNNING, PAUSED, STOPPED)
        self._start_time = 0  # Time that self.start() was called
        self._end_time = 0  # Time that self.end() was called
        self._pause_time = 0  # Time spent in pause
        self._total_pause_time = 0  # Total time spent in pause
        self._laps = []  # All laps
        self._lap_count = 0  # Total lap count, inclusive of the current lap

    def start(self, name="start"):
        """Starts the timer"""
        self.state = RUNNING
        self._start_time = get_current_time()  # Set the start time
        self.lap(name)  # Create a lap with this start time

    def end(self):
        """Ends the timer"""
        self.state = STOPPED
        self._end_time = get_current_time()  # Set the end time
        self._end_lap()  # end the last lap

    def lap(self, name=None):
        """Ends the current lap and creates a new lap in lap object"""
        self._end_lap()

        lap = {
            "name": name if name else self._lap_count,
            "start": get_current_time(),
            "end": -1,
            "total": -1,
        }

        self._laps.append(lap)
        self._lap_count += 1

    def _end_lap(self):
        """Assign end and total times to the previous lap"""
        self._lap_count = len(self._laps) - 1
        if len(self._laps) > 0:
            self._laps[self._lap_count]['end'] = get_current_time()
            self._laps[self._lap_count]['total'] = \
                self._laps[self._lap_count]['end'] - self._laps[self._lap_count]['start']

    def summary(self):
        """Returns a summary of all timer activity so far"""
        return {
            'running': self.state,
            'start': self._start_time,
            'end': self._end_time,
            'total': self._end_time - self._start_time,
            'paused': self._total_pause_time,
            'laps': self._laps
        }

    def pause(self):
        """Initiates a pause in the timer"""
        self.state = PAUSED
        self._pause_time = get_current_time()

    def unpause(self):
        """Cancels the pause previously set"""
        self.state = RUNNING
        self._total_pause_time = self._total_pause_time + (get_current_time() - self._pause_time)
        self._pause_time = 0
