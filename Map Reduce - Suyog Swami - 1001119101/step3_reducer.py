#!/usr/bin/env python

#------------------------------------------------------------------------------
#   Name: Suyog S Swami
#   Students ID: 1001119101
#   Programming Assignment 3- Data Mining - Map Reduce
#------------------------------------------------------------------------------

import sys
import re
count=0
for line in sys.stdin:
    line=line.strip()
    count=count+int(line)

print(count)