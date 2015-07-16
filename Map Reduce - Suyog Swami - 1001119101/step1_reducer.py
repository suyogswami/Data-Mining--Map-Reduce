#!/usr/bin/env python

#------------------------------------------------------------------------------
#   Name: Suyog S Swami
#   Students ID: 1001119101
#   Programming Assignment 3- Data Mining - Map Reduce
#------------------------------------------------------------------------------

from operator import itemgetter
import sys

node1=0
node2=0
nodelist=[]


for line in sys.stdin:
    nodelist.append(line)
for nl1 in nodelist:
    node1=None
    node2=None
    nl1out=nl1.strip()
    node1,node2=nl1out.split('\t',1)
    for nl2 in nodelist:
        nodeA=None
        nodeB=None
        nl2out=nl2.strip()
        nodeA,nodeB=nl2out.split('\t',1)
        if node1==nodeA and node2==nodeB:
            print('%s\t%s' %(nodeA,nodeB))
        elif node1==nodeB and node2==nodeA:
            continue
        elif node1 == nodeB:
            print('%s\t%s\t%s' %(node2,nodeA,nodeB))

