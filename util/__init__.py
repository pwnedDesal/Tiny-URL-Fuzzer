# coding: UTF-8

import os
from .fuzzer import Fuzzer
from subprocess import check_output, CalledProcessError


DEV_NULL = open(os.devnull, 'w')


def execute(lang, binary, url, base):
    if binary.startswith('self'):
        _, method_name = binary.split('.', 1)
        method_name = 'my_%s' % method_name
        fuzzer = Fuzzer()
        method = getattr(fuzzer, method_name)
        print(url)
        r = method(url)
    else:
        if lang.lower() == 'java':
            class_name = binary.split('.')[0]
            commands = ['java', '-cp', base, class_name, url]
        else:
            # print('init.py')
            # print(base + binary)
            commands = [base + binary, url]
        r = cmd(commands)
    return r


def cmd(cmd):
    try:
        res = check_output(cmd, stderr=DEV_NULL).strip()
    except CalledProcessError:
        res = 'err'
    except OSError:
        raise OSError('File Not Found: %s' % ' '.join(cmd))
    return res


def pprint(res):
    print('')
    for key in sorted(res):
        print('%-24s %s' % (key, res[key]))
    print('')
