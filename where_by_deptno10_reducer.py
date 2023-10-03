#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import sys

prev_deptno = None
dname = None
enames = []
# find the names of all employees who are not in the Finance department and have a salary greater than or equal to 5000
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
                if prev_deptno != '100' and int(salary) >= 5000:
                    for ename in enames:
                        print("{0}, {1}".format(ename, dname))
            dname = None
            enames = [ename]
            prev_deptno = deptno
    else:
        dname = table_value.split(",", maxsplit=1)[1]
        if prev_deptno and dname and enames:
            if prev_deptno != '100' and int(salary) >= 5000:
                for ename in enames:
                    print("{0}, {1}".format(ename, dname))
            prev_deptno = None
            enames = []
if prev_deptno and dname and enames:
    if prev_deptno != '100' and int(salary) >= 5000:
        for ename in enames:
            print("{0}, {1}".format(ename, dname))