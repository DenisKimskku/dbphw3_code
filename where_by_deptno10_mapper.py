#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import sys
for line in sys.stdin:
    line = line.strip()
    tuple_list = line.split(",")
    if len(tuple_list) == 11:
        ename = tuple_list[1] + ' ' + tuple_list[2]
        salary = tuple_list[-4]
        deptno = tuple_list[-1]
        if deptno != '100' and int(salary) >= 5000: # 100 indicates finance dept
            print("{0}\t{1}".format(ename, salary))
    else:
        pass
        #dname = tuple_list[1]
        #print("{0}\t{1}".format("NULL", dname))#may not need, just in case