import datetime

class Result:
    def __init__(self, result: bool, text: str):
        self.result = result
        self.text = text
        self.time = datetime.datetime.now()
        self.name = None

    def set_name(self, name):
        self.name = name
        return self

    @staticmethod
    def fail(text: str):
        return Result(False, text)

    @staticmethod
    def success(text: str):
        return Result(True, text)
