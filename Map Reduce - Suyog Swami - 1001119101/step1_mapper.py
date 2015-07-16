#!/usr/bin/env python

#------------------------------------------------------------------------------
#   Name: Suyog S Swami
#   Students ID: 1001119101
#   Programming Assignment 3- Data Mining - Map Reduce
#------------------------------------------------------------------------------

import sys
import re

for line in sys.stdin:
    line=line.strip()
    node1,node2 = line.split('\t',1)
    node1,node2=node2,node1
    print('%s\t%s' % (node1,node2))