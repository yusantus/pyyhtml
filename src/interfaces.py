from abc import ABC, abstractmethod

class FromFile(ABC):
    def __init__(self, filepath):
        self.filepath = filepath

    @abstractmethod
    def get_content_list(self):
        pass