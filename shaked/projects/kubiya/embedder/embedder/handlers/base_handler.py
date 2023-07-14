from abc import ABC, abstractmethod

class BaseHandler(ABC):
    @abstractmethod
    def handle_request(self, request):
        pass

