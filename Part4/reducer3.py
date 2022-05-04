#!/usr/bin/env python

"""reducer.py"""


# output the inverse document frequency of each term 

import sys
import math
# input comes from STDIN
for line in sys.stdin:
    line = line.strip()
    file_name, term, term_count, idf, num_terms_in_doc = line.split('\t')
    tf = int(term_count) / int(num_terms_in_doc)
    tf_idf = (float(tf)) * float(idf)
    print(f"(({file_name}, {term}), ({tf}, {idf}, {tf_idf}))")
    

  
    
