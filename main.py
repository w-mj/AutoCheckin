from result import Result
from shadowsky import ShadowSky
from notifier import ConsoleNotifier
from checkin import Checker
import sys


assigned_list = [ShadowSky]


def build_argv():
    ret = {}
    if len(sys.argv) < 2:
        return
    argv_list = sys.argv[1].split('|')
    for argv in argv_list:
        argv.strip(' \n\r')
        equal = argv.find('=')
        if equal == -1:
            raise Exception("can not parse argument {}".format(argv))
        plus = argv[:equal].find('+')
        if plus == -1:
            raise Exception("Can not parse argument {}".format(argv))
        cls = argv[:plus]
        arg = argv[plus+1:equal]
        val = argv[equal+1:]
        if cls not in ret:
            ret[cls] = {}
        ret[cls][arg] = val
    return ret


def main():
    notifier = ConsoleNotifier()
    checker = Checker(notifier)
    argv = build_argv()
    for assigned_class in assigned_list:
        class_name = assigned_class.__name__
        try:
            checker.assign(assigned_class(**(argv.get(class_name, {}))))
        except Exception as e:
            result = Result(False, str(e)).set_name(class_name)
            notifier.add_notify(result)

    checker.checkin_all()
    notifier.notify()


if __name__ == '__main__':
    main()
