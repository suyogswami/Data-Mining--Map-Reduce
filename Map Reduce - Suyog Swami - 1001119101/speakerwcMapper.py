#!/usr/bin/env python

#------------------------------------------------------------------------------
#   Name: Suyog S Swami
#   Students ID: 1001119101
#   Programming Assignment 3- Data Mining - Map Reduce
#------------------------------------------------------------------------------

import sys
import re
stopwords = ["i", "me", "my", "myself", "we", "our", "ours", "ourselves", \
            "you", "your", "yours", "yourself", "yourselves", "he", "him", \
            "his", "himself", "she", "her", "hers", "herself", "it", "its", \
            "itself", "they", "them", "their", "theirs", "themselves", "what",\
            "which", "who", "whom", "this", "that", "these", "those", "am", "is",\
            "are", "was", "were", "be", "been", "being", "have", "has", "had",\
            "having", "do", "does", "did", "doing", "a", "an", "the", "and", "but",\
            "if", "or", "because", "as", "until", "while", "of", "at", "by", "for", \
            "with", "about", "against", "between", "into", "through", "during", "before", \
            "after", "above", "below", "to", "from", "up", "down", "in", "out", "on", "off", \
            "over", "under", "again", "further", "then", "once", "here", "there", "when", "where", \
            "why", "how", "all", "any", "both", "each", "few", "more", "most", "other","some", "such", \
            "no", "nor", "not", "only", "own", "same", "so", "than", "too", "very", "s", "t", "can", "will", "just", "don", "should", "now"]
for line in sys.stdin:
    line = line.strip()
    speaker,debate = line.split(':',1)
    words = re.findall(r"[\'A-Za-z]+", debate)
    for word in words:
        word=word.lower()
        if word not in stopwords:
            print('%s:%s\t%s' % (speaker,word, 1))