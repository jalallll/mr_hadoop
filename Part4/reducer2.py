#!/usr/bin/env python

"""reducer.py"""


# output the inverse document frequency of each term 

import sys
import math
for line in sys.stdin:
  line = line.strip()
  word, file_name, count, numFiles, num_doc_occurrence = line.split('\t')
  numFiles = int(numFiles)
  num_doc_occurrence = int(num_doc_occurrence)
  inverse_doc_freq = math.log(numFiles / num_doc_occurrence, 10)
  print('%s\t%s\t%s\t%s' % (file_name, word, count, inverse_doc_freq))

  
    
