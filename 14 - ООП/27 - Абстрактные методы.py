from abc import ABC, abstractmethod


class User(ABC):

    def __init__(self):
        super().__init__()


    @abstractmethod
    def login(self):
        print('User logged in')

    @abstractmethod
    def logout(self):
        print('User logged out')

c = User()
