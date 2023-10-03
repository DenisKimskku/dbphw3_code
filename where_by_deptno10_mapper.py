#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import sys
dept_dict = {}
for line in sys.stdin:
    line = line.strip()
    tuple_list = line.split(",")
    if len(tuple_list) == 11:
        ename = tuple_list[1] + ' ' + tuple_list[2]
        salary = tuple_list[-4]
        deptno = tuple_list[-1]
        value = ','.join(['emp', ename, salary])
        if deptno in dept_dict:
            dept_dict[deptno].append(value)
        else:
            dept_dict[deptno] = [value]
    else:
        dname = tuple_list[1]
        deptno = tuple_list[0]
        value = ','.join(['dept', dname])
        if deptno in dept_dict:
            for emp in dept_dict[deptno]:
                print('{0}\t{1}'.format(deptno, emp + ',' + value))
            del dept_dict[deptno]
        else:
            print('{0}\t{1}'.format(deptno, ',' + value))