#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import sys

prev_deptno = None
dname = None
enames = []

for line in sys.stdin:
    line = line.strip()
    deptno, table_value = line.split("\t", maxsplit=1)
    table = table_value.split(",", maxsplit=1)[0]
    if table == 'emp':
        ename, salary = table_value.split(",", maxsplit=2)[1:]
        enames.append(ename)
    else:
        dname = table_value.split(",", maxsplit=1)[1]
        if enames:
            for ename in enames:
                print("{0}, {1}".format(ename, dname))
        else:
            print("{0}, {1}".format("NULL", dname))
        enames = []
if dname and enames:
    for ename in enames:
        print("{0}, {1}".format(ename, dname))