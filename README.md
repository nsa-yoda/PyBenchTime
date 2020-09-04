PyBenchTime v0.0.1
===================

[![License](https://poser.pugx.org/jsanc623/phpbenchtime/license.svg)](https://packagist.org/packages/jsanc623/phpbenchtime)

A light benchmark timer class for Python. PyBenchTime is quite simple to use and is loaded with functionality
- including detailed summary data, readable source, a lap system and pause/unpause functionality.
This is the Python version of the popular [PHPBenchTime](https://github.com/jsanc623/PHPBenchTime) PHP Package.

Package Methods and Properties
=======
```
get_current_time()
```

Class Methods and Properties
=======
```
start()           # Starts the timer
end()             # Ends the timer
lap(name=None)    # Creates a lap w/ optional name
summary()         # Outputs a summary of timing and laps
pause()           # Pauses the timer
unpause()         # Unpauses the timer
_end_lap()        # Ends a lap (private)
_start_time       # The time we started the timer (private)
_end_time         # The time we ended the timer (private)
_pause_time       # The time we paused the timer (private)
_total_pause_time # The total time we've spent paused (private)
_laps             # The laps and all their data (private)
_lap_count        # The total number of laps (private)
```


Quickstart
=====

Load and initiate the PyBenchTime Timer:
```
from PyBenchTime import Timer
T = Timer()
```

That was easy! Now lets start a new timer:
```
T.start()
```

Then lets just sleep for 3 seconds:
```
import time
time.sleep(3)
```

Now, lets end the timer, and put results in `time`:
```
time = T.end()
```

When we end a timer, we receive a dict back, containing the start time,
end time and difference between start and end times:
```
{
    [running] => false
    [start] => 1406146951.9998
    [end] => 1406146952.0638
    [total] => 0.0019998550415039
    [paused] => 0
    [laps] => {
        [0] => {
            [name] => start
            [start] => 1406146951.9998
            [end] => 1406146952.0018
            [total] => 0.0019998550415039
        }
    }
}
```

Advanced Usage: Laps
=====================

PyBenchTime also allows you to set laps between code execution, which allows 
you to determine what part of your code is causing a bottleneck.

Let's sleep for a couple of seconds between laps and end the timer
```
sleep(1);
T.lap();
sleep(2);
T.lap();
time = T.end();
```

Let's see the results:
```
{
    [running] => false
    [start] => 1406146951.9998
    [end] => 1406146952.0638
    [total] => 0.063999891281128
    [paused] => 0.041000127792358
    [laps] => {
        [0] => {
            [name] => start
            [start] => 1406146951.9998
            [end] => 1406146952.0018
            [total] => 0.0019998550415039
        },
        [1] => {
            [name] => 1
            [start] => 1406146952.0018
            [end] => 1406146952.0028
            [total] => 0.0010001659393311
        },
        [2] => {
            [name] => 2
            [start] => 1406146952.0028
            [end] => 1406146952.0128
            [total] => 0.0099999904632568
        }
    }
}
```

Advanced Usage
==============
PyBenchTime allows you to do named laps, as well as to pause and unpause the timer. This comes in handy when you want 
to make a network call or a call out to the database for instance, but don't want to include that time in your 
benchmark - pause and then unpause after you receive the network/database data.