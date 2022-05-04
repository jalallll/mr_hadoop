#!/usr/bin/env python

#output the terms in each doc and the total number of files

import sys
import os 

import glob

# inputDirectory is where text files for testing are located 

inputPath = os.getcwd() + "/inputDirectory"

inputDir = glob.glob(inputPath+"/*")

files = []

for file in inputDir:
    files.append(file)

for file in inputDir:
    fp = open(file)
    for line in fp:
        line = line.strip()

        words = line.split()

        for word in words:
            file_name = file.split('/')[-1]
            print('%s\t%s\t%s\t%s' % (word,file_name,1, len(files))) 

    
        
