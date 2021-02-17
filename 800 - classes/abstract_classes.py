import abc


class AbstractClass(abc.ABC):
    @abc.abstractmethod
    def abstract_method1(self):
        """undefined method"""

    def defined_method(self):
        return 'defined return value'


class DefinedClass(AbstractClass):
    pass


if __name__ == '__main__':
    # a = AbstractClass()
    b = DefinedClass()

    assert isinstance(b, AbstractClass)
