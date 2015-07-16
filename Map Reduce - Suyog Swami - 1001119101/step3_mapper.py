#!/usr/bin/env python

#------------------------------------------------------------------------------
#   Name: Suyog S Swami
#   Students ID: 1001119101
#   Programming Assignment 3- Data Mining - Map Reduce
#------------------------------------------------------------------------------

import sys
import re

for line in sys.stdin:
    node1,node2,node3,node4=None,None,None,None
    line=line.strip()
    node1,node2,node3,node4=line.split('\t',3)
    print(node4)