import json

from main import Timer, get_current_time, RUNNING, PAUSED, STOPPED
from time import time, sleep


def test_get_current_time():
    assert get_current_time() == time()


def test_start():
    t = Timer()
    t.start()
    assert t.state == RUNNING


def test_end():
    t = Timer()
    t.start()
    sleep(2)
    t.end()

    assert t.summary()["running"] == -1
    assert t.summary()["paused"] == 0
    assert len(t.summary()["laps"]) == 1
    assert t.summary()["laps"][0]["name"] == "start"
    assert t.summary()["laps"][0]["start"] - t.summary()["start"] < 0.00005
    assert t.summary()["laps"][0]["end"] - t.summary()["end"] < 0.00005


def test_lap():
    t = Timer()
    t.lap()
    sleep(0.25)
    t.lap("some lap")
    sleep(0.25)
    t.lap()
    sleep(0.25)
    t.lap()
    sleep(0.25)
    t.lap()
    sleep(0.25)
    t.lap()
    sleep(0.25)
    t.end()

    assert t.summary()["running"] == -1
    assert t.summary()["paused"] == 0
    assert len(t.summary()["laps"]) == 6
    assert t.summary()["laps"][0]["name"] == 0
    assert t.summary()["laps"][1]["name"] == "some lap"


def test_summary():
    t = Timer()
    t.start()
    t.lap()
    sleep(0.25)

    assert t.summary()["running"] == 1
    assert t.summary()["paused"] == 0
    assert len(t.summary()["laps"]) == 2
    assert t.summary()["laps"][0]["name"] == "start"

    t.end()

    assert t.summary()["running"] == -1
    assert t.summary()["paused"] == 0
    assert len(t.summary()["laps"]) == 2


def test_pause():
    t = Timer()
    t.start()
    sleep(0.25)

    assert t.summary()["running"] == 1
    assert t.summary()["paused"] == 0

    t.pause()
    sleep(0.25)

    assert t.summary()["running"] == 0
    assert t.summary()["paused"] == 0

    t.unpause()

    assert t.summary()["running"] == 1
    assert t.summary()["paused"] > 0.25


def test_unpause():
    t = Timer()
    t.start()
    sleep(0.25)
    t.unpause()
    assert t.summary()["running"] == 1
    assert t.summary()["paused"] == 0
