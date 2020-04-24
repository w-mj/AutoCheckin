from abc import abstractmethod

from notifier import Notifier
from result import Result


class Checkin:
    def __init__(self, name: str):
        self.name = name

    @abstractmethod
    def checkin(self) -> Result:
        pass


class Checker:
    def __init__(self, notifier: Notifier):
        self.instances = []
        self.notifier = notifier

    def assign(self, cls: Checkin):
        self.instances.append(cls)
        return self

    def checkin_all(self):
        # 执行所有签到
        for x in self.instances:
            try:
                res = x.checkin()
            except Exception as e:
                res = Result.fail(str(e))
            res.set_name(x.name)
            self.notifier.add_notify(res)
        return self
