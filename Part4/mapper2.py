#!/usr/bin/env python

import sys

# This file will output the number of documents that contain a specific term t

# term doc list
td = []

prev_term = None
prev_file = None 
file_name = None
term = None
prev_term_freq = 0

num_files = 0

def print_out():
  global td
  global prev_term 
  global num_files
  for entry in td:
    print('%s\t%s\t%s\t%s\t%s' % (prev_term, entry[0], entry[1], num_files, len(td)))


def main():
  global td
  global prev_term 
  global prev_file 
  global prev_term_freq
  global num_files
  global term 
  global file_name
  for line in sys.stdin:
    line.strip()
    term, file_name, term_freq, num_files = line.split('\t')
    term_freq = int(term_freq)
    num_files = int(num_files)
    if prev_term == term:
      td.append([file_name, term_freq])
    else:
      if prev_term and prev_file:
        print_out()
      prev_term_freq = term_freq
      prev_term = term 
      prev_file = file_name 
      td.clear()
      td.append([file_name, term_freq])

  if prev_term == term:
    print_out()




if __name__ == "__main__":
    main()



  



  


