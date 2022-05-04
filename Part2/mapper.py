#!/usr/bin/env python

import sys


prev_word = ""

for line in sys.stdin:
  words = line.strip().split()

  for i in range(len(words)):
    if i==0:
        if prev_word!="":
          print('%s %s\t%s' % (prev_word.strip(), words[i].strip(), 1))
    else:
      if i==len(words)-1:
        prev_word = words[i]
      print('%s %s\t%s' % (words[i-1].strip(), words[i].strip(), 1))
      
  

    

