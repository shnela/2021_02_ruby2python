"""
https://book.pythontips.com/en/latest/__slots__magic.html
Result:
    Class dict used 295.104512 MB.
    Class EventSlots used 99.803136 MB.
    Class EventTuple used 116.097024 MB.
    Class Event used 213.635072 MB.
"""
import os
import random
from collections import namedtuple
from multiprocessing import Pool

import psutil

DNA_BASES = 'ATCG'


class Event:
    def __init__(self, dna_base, value):
        self.dna_base = dna_base
        self.value = value


class EventSlots:
    __slots__ = ['dna_base', 'value']

    def __init__(self, dna_base, value):
        self.dna_base = dna_base
        self.value = value


EventTuple = namedtuple('EventTuple', ['dna_base', 'value'])


def generate_events(event_cls: type, events_no: int = 10 ** 6):
    events = [
        event_cls(dna_base=random.choice(DNA_BASES), value=i)
        for i in range(events_no)
    ]
    process = psutil.Process(os.getpid())
    process_size = process.memory_info().rss / 10 ** 6  # in MB
    print(f"Class {event_cls.__name__} used {process_size} MB.")


if __name__ == '__main__':
    with Pool(5) as p:
        p.map(generate_events, [dict, Event, EventSlots, EventTuple])
