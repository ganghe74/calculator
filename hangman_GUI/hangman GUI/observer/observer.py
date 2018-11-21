from abc import ABCMeta, abstractmethod


class Observer(metaclass=ABCMeta):
    """ Abstract Observer class"""

    @abstractmethod
    def update(self, model):
        pass
