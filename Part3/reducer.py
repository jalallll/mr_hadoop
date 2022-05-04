#!/usr/bin/env python


import sys
import os 

bigrams = {}

def print_bigram_freq():
  sorted_bigrams = sorted(list(bigrams.keys()))
  for bigram_pair in sorted_bigrams:
    # check if unique bigram
    if bigrams[bigram_pair] == 1:
      print(f"(({bigram_pair}), {bigrams[bigram_pair]})")

    
def main():
  for line in sys.stdin:
    bigram, count = line.strip().split('\t')
    if bigram in bigrams:
      bigrams[bigram] += 1
    else:
      bigrams[bigram] = 1
  print_bigram_freq()

  

if __name__ == "__main__":
    main()