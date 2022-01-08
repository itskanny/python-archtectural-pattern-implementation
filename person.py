from abc import ABC, abstractmethod


class Person(ABC):

    def __init__(self, id=None, email=None, name=None):
        self.id = id
        self.name = name
        self.email = email

    @abstractmethod
    def update(self):
        pass

    @abstractmethod
    def create(self):
        pass

    @abstractmethod
    def delete(self):
        pass

    @abstractmethod
    def view(self):
        pass
