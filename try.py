#!/usr/local/bin/python3.9
# coding: UTF-8
import sys
# ty
from util import pprint, execute
from const import PARSERS, REQUESTERS
url = sys.argv[1]
res = {}
for key, binary in PARSERS.items():
    lang, libname = key.split('.', 1)
    r = execute(lang, binary, url, base='bin/parser/')
    res[key] = r
pprint(res)

res = {}
for key, binary in REQUESTERS.items():
    lang, libname = key.split('.', 1)
    r = execute(lang, binary, url, base='bin/requester/')
    res[key] = r
pprint(res)
