#!/usr/bin/env python

"""reducer.py"""

from operator import itemgetter
import sys
import os 

prev_count = 0
prev_file = None
prev_word = None
# input comes from STDIN
for line in sys.stdin:
    line = line.strip()
    word, file_name, count = line.split('\t')
  
    if prev_file==file_name and prev_word==word:
        prev_count += 1
    else:
        if prev_word and prev_file:
            print(f"(({prev_word}, {prev_file}) {prev_count})")
        prev_count = 1
        prev_word = word
        prev_file = file_name
    

# print the word properties of the last line we read
if prev_file==file_name and prev_word==word:
    print(f"(({prev_word}, {prev_file}) {prev_count})")
