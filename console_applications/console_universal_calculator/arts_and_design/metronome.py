import math
import time
import winsound


def metronome(bpm, duration_secs):

    interval = 60 / bpm
    bps = bpm / 60
    total_beats = int(bps * duration_secs)

    if 1 <= bpm <= 600:
        for i in range(0, total_beats):
            winsound.MessageBeep(winsound.MB_OK)
            time.sleep(interval)
    else:
        return "Beats per minute must be >= 1 and <= 600"
