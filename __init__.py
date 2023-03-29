from main import Timer, PAUSED, RUNNING, STOPPED, get_current_time


def int_or_str(value):
    try:
        return int(value)
    except ValueError:
        return value


__version__ = "1.0.0"
VERSION = tuple(map(int_or_str, __version__.split(".")))

__all__ = ["Timer", "STOPPED", "RUNNING", "PAUSED", "get_current_time"]
