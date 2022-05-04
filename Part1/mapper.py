#!/usr/bin/env python
"""mapper.py"""

import sys
import os 


# input comes from STDIN (standard input)
for line in sys.stdin:

    line = line.strip()

    words = line.split()

    for word in words:
        file_path = os.environ.get('map_input_file')
        file_path = str(file_path)
        file_name = file_path.split("/")[-1]
        print('%s\t%s\t%s' % (word,file_name,1))

    
        
