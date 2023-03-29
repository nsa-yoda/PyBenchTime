from time import time

# Handle the running state of the timer
RUNNING = 1
PAUSED = 0
STOPPED = -1


def get_current_time():
    return time()


class Timer:
    def __init__(self):
        # Maintains the state of the timer (RUNNING, PAUSED, STOPPED)
        self.state = STOPPED

        # Time that self.start() was called
        self._start_time = 0

        # Time that self.end() was called
        self._end_time = 0

        # Time spent in pause
        self._pause_time = 0

        # Total time spent in pause
        self._total_pause_time = 0

        # All laps
        self._laps = {}

        # Total lap count, inclusive of the current lap
        self._lap_count = -1

    def start(self, name="start", lap=True):
        """Starts the timer"""
        self.state = RUNNING
        self._start_time = get_current_time()

        # Create a lap with this start time
        if lap:
            self.lap(name)

    def end(self):
        """Ends the timer"""
        self.state = STOPPED
        self._end_time = get_current_time()
        self._lap_count += 1
        self._end_lap()

    def lap(self, name=None):
        """Ends the current lap and creates a new lap in lap object"""
        if self._start_time == 0:
            self.start(lap=False)

        self._lap_count += 1
        self._end_lap()

        lap = {
            "name": name if name else self._lap_count,
            "start": get_current_time(),
            "end": -1,
            "total": -1,
        }

        self._laps[self._lap_count] = lap

    def _end_lap(self):
        """Assign end and total times to the previous lap"""
        if len(self._laps) > 0:
            self._laps[self._lap_count - 1]["end"] = get_current_time()
            self._laps[self._lap_count - 1]["total"] = (
                self._laps[self._lap_count - 1]["end"]
                - self._laps[self._lap_count - 1]["start"]
            )

    def summary(self):
        """Returns a summary of all timer activity so far"""
        return {
            "running": self.state,
            "start": self._start_time,
            "end": self._end_time,
            "total": self._end_time - self._start_time,
            "paused": self._total_pause_time,
            "laps": self._laps,
        }

    def pause(self):
        """Initiates a pause in the timer"""
        self.state = PAUSED
        self._pause_time = get_current_time()

    def unpause(self):
        """Cancels the pause previously set"""
        if self.state == PAUSED:
            self.state = RUNNING
            self._total_pause_time = self._total_pause_time + (
                get_current_time() - self._pause_time
            )
            self._pause_time = 0

    def pretty_summary(self, json):
        """an unrelated pretty print helper, yes you have to pass in THE json package"""
        return json.dumps(self.summary(), indent=2)
