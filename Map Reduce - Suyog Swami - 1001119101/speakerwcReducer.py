#!/usr/bin/env python

#------------------------------------------------------------------------------
#   Name: Suyog S Swami
#   Students ID: 1001119101
#   Programming Assignment 3- Data Mining - Map Reduce
#------------------------------------------------------------------------------

from operator import itemgetter
import sys

current_speakerWord = None
current_speakerWordCount = 0
speakerWord = None

for line in sys.stdin:
    line = line.strip()

    speakerWord, speakerWordCount= line.split('\t', 1)

    try:
        speakerWordCount = int(speakerWordCount)
    except ValueError:
        continue

    if current_speakerWord == speakerWord:
        current_speakerWordCount += speakerWordCount
    else:
        if current_speakerWord and current_speakerWordCount>200:
            print ('%s\t%s' % (current_speakerWord, current_speakerWordCount))
        current_speakerWordCount = speakerWordCount
        current_speakerWord = speakerWord

if current_speakerWord == speakerWord and current_speakerWordCount>200:
    print ('%s\t%s' % (current_speakerWord, current_speakerWordCount))


#Most of the code is from the reducer.py provided by prof. Chengkai Li. I have just modified whereever required.
