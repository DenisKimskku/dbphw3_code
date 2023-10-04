#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import sys
sig_flag = False
for line in sys.stdin:
    line = line.strip()
    tuple_list = line.split(",")
    if len(tuple_list) == 11:
        ename = tuple_list[1] + ' ' + tuple_list[2]
        salary = int(tuple_list[-4])
        deptno = tuple_list[-1]
        if deptno != '100' and int(salary) >= 5000:
            value = ','.join(['emp', ename, str(salary)])
            print('{0}\t{1}'.format(deptno, value))
            sig_flag = True
    else:
        if sig_flag is False:
            continue
        dname = tuple_list[1]
        deptno = tuple_list[0]
        value = ','.join(['dept', dname])
        print('{0}\t{1}'.format(deptno, value))
        sig_flag = False