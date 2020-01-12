#!/usr/bin/env python3
# Filename: run_treetagger.py
# Author: #cf

"""
Create a derived format from full, annotated text.
"""

# ====================================
# IMPORTS
# ====================================

import glob
import os
import re
import csv
import pandas as pd
import numpy as np
from os.path import join
import random

# ====================================
# FUNCTIONS
# ====================================


def get_filename(textfile):
    filename, ext = os.path.basename(textfile).split(".")
    return filename


def read_text(textfile):
    with open(textfile, "r") as infile:
        tagged = infile.read()
        return tagged


def create_segments(tagged, params): 
    segments = [tagged[x:x+params["seglen"]] for x in range(0, len(tagged), params["seglen"])]
    return segments


def scramble_segments(segments, params): 
    scrambled = []
    for seg in segments: 
        random.shuffle(seg) # scrambling
        seg = "\n".join(seg)
        scrambled.append(seg)
    return scrambled
   

def save_scrambled(scrambled, srcfolder, filename):
    filepath = join(srcfolder, filename+".txt")
    scrambled = "\n<SEG>\n".join(scrambled)    
    with open(filepath, "w", encoding="utf-8") as outfile:
        outfile.write(scrambled)


# ====================================
# MAIN
# ====================================

def main(sourcefolder, srcfolder, params):
    print("\nformats1_tdm")
    if not os.path.exists(srcfolder):
        os.makedirs(srcfolder)
    for textfile in glob.glob(join(sourcefolder, "*.txt")):
        filename = get_filename(textfile)
        print("--"+filename)
        tagged = read_text(textfile).split("\n")
        segments = create_segments(tagged, params)
        scrambled = scramble_segments(segments, params)
        save_scrambled(scrambled, srcfolder, filename)

if __name__ == "__main__":
    main(sourcefolder, srcfolder, params)
