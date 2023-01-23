import os

import yaml

from airtcp import AirTCP
from checkin import Checker
from notifier import ConsoleNotifier
from result import Result
from shadowsky import ShadowSky

assigned_list = [ShadowSky, AirTCP]


def main():
    notifier = ConsoleNotifier()
    checker = Checker(notifier)
    accounts = yaml.safe_load(os.environ["SECRET"])
    for assigned_class in assigned_list:
        class_name = assigned_class.__name__
        try:
            checker.assign(assigned_class(**(accounts.get(class_name, {}))))
        except Exception as e:
            result = Result(False, str(e)).set_name(class_name)
            notifier.add_notify(result)

    checker.checkin_all()
    notifier.notify()


if __name__ == "__main__":
    main()
