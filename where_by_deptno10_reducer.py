#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import sys

for line in sys.stdin:
    line = line.strip()
    deptno, table_value = line.split("\t", maxsplit=1)
    if deptno == '10':
        table, value = table_value.split(",", maxsplit=1)
        if table == 'emp':
            ename, salary = value.split(",", maxsplit=2)[1:]
            print("{0}, {1}".format(ename, salary))
        else:
            dname = value.split(",", maxsplit=1)[1]
            print("{0}, {1}".format("NULL", dname))