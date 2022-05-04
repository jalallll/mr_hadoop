#!/usr/bin/env python

import sys

# This file will output the number of terms that are in a specific doc 

# term doc list
td = []

prev_term = None
prev_file = None 
file_name = None

prev_term_freq = 0

idf = 0

def print_out():
  global td
  global prev_file 
  global idf

  for entry in td:
    print('%s\t%s\t%s\t%s\t%s' % (prev_file, entry[0], entry[1], entry[2], sum_term_freq()))

def sum_term_freq():
  sum_tf = 0
  for entry in td:
    sum_tf += entry[1]
  return sum_tf


def main():
  global td
  global prev_term 
  global prev_file 
  global prev_term_freq
  global idf
  global file_name 

  for line in sys.stdin:
    line.strip()
    file_name, term, term_freq, idf = line.split('\t')
    term_freq = int(term_freq)
    idf = float(idf)

    if prev_file == file_name:
      td.append([term, term_freq, idf])
    else:
      if prev_term and prev_file:
        print_out()
      prev_term_freq = term_freq
      prev_term = term 
      prev_file = file_name 
      td.clear()
      td.append([term, term_freq, idf])

  if prev_file == file_name:
    print_out()




if __name__ == "__main__":
    main()



  



  


