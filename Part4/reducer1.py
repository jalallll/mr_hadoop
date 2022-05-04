#!/usr/bin/env python



# output the terms in each doc and their frequency

import sys

prev_count = 0
prev_file = None
prev_word = None

# input comes from STDIN
for line in sys.stdin:
    line = line.strip()
    word, file_name, count, numFiles = line.split('\t')
  
    # if the newly read line has the same word and file as the previously read line
    if prev_file==file_name and prev_word==word:
        prev_count += 1
    # if newly read line has word and file that is different than the previously read line
    else:
        # check if we read a word and file before this line, if so then print that
        if prev_word and prev_file:
            print('%s\t%s\t%s\t%s' % (prev_word,prev_file,prev_count, numFiles))
        # we will consider the newly read word and its properties in next loop iteration
        prev_count = 1
        prev_word = word
        prev_file = file_name
        
# print the word properties of the last line we read
if prev_file==file_name and prev_word==word:
    print('%s\t%s\t%s\t%s' % (prev_word,prev_file,prev_count, numFiles))


