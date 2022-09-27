from abc import ABC, abstractmethod


class IDBConnection(ABC):

    @abstractmethod
    def connect(self):
        raise NotImplementedError

    def is_up(self):
        raise NotImplementedError

    def disconnect(self):
        raise NotImplementedError
