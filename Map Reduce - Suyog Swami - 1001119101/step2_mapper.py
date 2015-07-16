#!/usr/bin/env python

#------------------------------------------------------------------------------
#   Name: Suyog S Swami
#   Students ID: 1001119101
#   Programming Assignment 3- Data Mining - Map Reduce
#------------------------------------------------------------------------------

import sys
import re
nodelist=[]
for line in sys.stdin:
    nodelist.append(line)

for ndlst in nodelist:
    node1,node2=None,None
    ndlst.strip()
    node1,node2=ndlst.split('\t',1)
    node2=node2.strip()
    if node2.find('\t')==-1:
        for nlst in nodelist:
            nodeA,nodeB,nodeC=None,None,None
            nlst.strip()
            nodeA,nodeB=nlst.split('\t',1)
            if nodeB.find('\t')!=-1:
                nodeB,nodeC=nodeB.split('\t',1)
                if node1==nodeA and node2==nodeB and nodeC!= None:
                    nodeC=nodeC.strip()
                    print('%s\t%s\t%s'%(nodeA,nodeB,nodeC))