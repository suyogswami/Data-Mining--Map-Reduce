#!/usr/bin/env python

#------------------------------------------------------------------------------
#   Name: Suyog S Swami
#   Students ID: 1001119101
#   Programming Assignment 3- Data Mining - Map Reduce
#------------------------------------------------------------------------------

import sys
import re
nodelist=[]
trilist=[]
final_count=0
lastlist=[]

for line in sys.stdin:
    nodelist.append(line)

#print(nodelist)

for nlt in nodelist:
    count=0
    node1,node2,node3=None,None,None
    nlt.strip()
    node1,node2=nlt.split('\t',1)
    if node2.find('\t')!=-1:
        node2,node3=node2.split('\t',1)
        node3=node3.strip()
    nodestr=str(node1)+'\t'+str(node2)+'\t'+str(node3)+'\n'
    #print(nodestr)
    if nodestr in nodelist:
        count=count+1
        #print(str(node3)+'\t'+str(node1)+'\t'+str(node2)+'\n')
        nodelist.remove(str(node3)+'\t'+str(node1)+'\t'+str(node2)+'\n')
        nodelist.remove(str(node2)+'\t'+str(node3)+'\t'+str(node1)+'\n')
        trilist.append('%s\t%s\t%s'%(node1,node2,count))
#print(nodelist)
#print(trilist)

for t in trilist:
    t=t.strip()
    nodex,nodey,count=t.split('\t',2)
    final_count=trilist.count(t)
    if ('1\t'+str(nodex)+'\t'+str(nodey)+'\t'+str(final_count)) not in lastlist:
        lastlist.append('1\t'+str(nodex)+'\t'+str(nodey)+'\t'+str(final_count))

for l in lastlist:
    print(l)


