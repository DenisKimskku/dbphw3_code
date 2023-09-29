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
        if prev_deptno == deptno:
            enames.append(ename)
        else:
            if prev_deptno and dname and enames:
                for ename in enames:
                    print("{0}, {1}".format(ename, dname))
            dname = None
            enames = [ename]
            prev_deptno = deptno
    else:
        dname = table_value.split(",", maxsplit=1)[1]
        if prev_deptno and dname and enames:
            for ename in enames:
                print("{0}, {1}".format(ename, dname))
if prev_deptno and dname and enames:
    for ename in enames:
        print("{0}, {1}".format(ename, dname))