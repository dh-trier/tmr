#!/usr/bin/env python3
# Filename: run_treetagger.py
# Author: #cf

"""
Create annotated text from plain text. 
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
import treetaggerwrapper
from os.path import join


# ====================================
# FUNCTIONS
# ====================================


def get_filename(textfile):
    filename, ext = os.path.basename(textfile).split(".")
    return filename


def read_text(textfile):
    with open(textfile, "r") as infile:
        text = infile.read()
        return text


def apply_tagger(text, params): 
    tagger = treetaggerwrapper.TreeTagger(TAGLANG=params["lang"])
    tagged = tagger.tag_text(text)
    tagged = "\n".join(tagged)
    return tagged


def save_tagged(tagged, taggedfolder, filename): 
    filepath = join(taggedfolder, filename+".txt")
    with open(filepath, "w", encoding="utf-8") as outfile:
        outfile.write(tagged)
    

# ====================================
# MAIN
# ====================================

def main(plainfolder, taggedfolder, params):
    print("\nformats0_tagging")
    if not os.path.exists(taggedfolder):
        os.makedirs(taggedfolder)
    allcounts = {}
    for textfile in glob.glob(join(plainfolder, "*.txt")):
        filename = get_filename(textfile)
        print("--"+filename)
        text = read_text(textfile)
        tagged = apply_tagger(text, params)
        save_tagged(tagged, taggedfolder, filename)

if __name__ == "__main__":
    main(plainfolder, taggedfolder, params)
