import abc
from collections import abc as cabc


class GenericAirplane(metaclass=abc.ABCMeta):
    @classmethod
    def __subclasshook__(cls, subclass):
        return (hasattr(subclass, 'flight') and callable(subclass.flight))


class A10:
    def flight(self):
        # https://www.youtube.com/watch?v=NvIJvPj_pjE
        return 'brrrrrrrrrrrrrt'


if __name__ == '__main__':
    a10 = A10()
    assert isinstance(a10, GenericAirplane)
