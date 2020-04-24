from abc import abstractmethod

from result import Result


class Notifier:

    @abstractmethod
    def add_notify(self, result: Result):
        pass

    @abstractmethod
    def notify(self):
        pass


class ConsoleNotifier(Notifier):

    def __init__(self):
        self.results = []

    def add_notify(self, result: Result):
        print("name: {}, result: {}, text: {}, time: {}".format(
            result.name, result.result, result.text, result.time))

    def notify(self):
        pass
