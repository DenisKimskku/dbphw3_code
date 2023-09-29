#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import sys

emp_dict = {}
for line in sys.stdin:
    line = line.strip()
    tuple_list = line.split(",")
    if len(tuple_list) == 11:
        ename = tuple_list[1] + ' ' + tuple_list[2]
        salary = tuple_list[-4]
        deptno = tuple_list[-1]
        value = ','.join(['emp', ename, salary])
        if deptno in emp_dict:
            emp_dict[deptno].append(value)
        else:
            emp_dict[deptno] = [value]
    else:
        dname = tuple_list[1]
        deptno = tuple_list[0]
        value = ','.join(['dept', dname])
        if deptno in emp_dict:
            for emp in emp_dict[deptno]:
                print('{0}\t{1}'.format(deptno, emp + ',' + value))
            del emp_dict[deptno]
        else:
            print('{0}\t{1}'.format(deptno, ',' + value))

for deptno in emp_dict:
    for emp in emp_dict[deptno]:
        print('{0}\t{1}'.format(deptno, emp + ','))