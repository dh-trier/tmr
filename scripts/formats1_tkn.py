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
from collections import Counter

# ====================================
# FUNCTIONS
# ====================================


def get_filename(textfile):
    filename, ext = os.path.basename(textfile).split(".")
    return filename


def read_text(textfile):
    with open(textfile, "r") as infile:
        tagged = infile.read().split("\n")
        tagged = [token for token in tagged if token]
        return tagged


def select_features(tagged, params):
    if params["token"] == "lemma": 
        features = [token.split("\t")[2] for token in tagged if len(token.split("\t"))==3]
    elif params["token"] == "pos": 
        features = [token.split("\t")[1] for token in tagged if len(token.split("\t"))==3]
    features = "\n".join(features)    
    return features


def save_features(features, tknfolder, filename): 
    filepath = join(tknfolder, filename+".txt")
    with open(filepath, "w", encoding="utf-8") as outfile:
        outfile.write(features)
    

# ====================================
# MAIN
# ====================================

def main(sourcefolder, tknfolder, params):
    print("\nformats1_tkn")
    if not os.path.exists(tknfolder):
        os.makedirs(tknfolder)
    allcounts = {}
    for textfile in glob.glob(join(sourcefolder, "*.txt")):
        filename = get_filename(textfile)
        print("--"+filename)
        tagged = read_text(textfile)
        features = select_features(tagged, params)
        save_features(features, tknfolder, filename)

if __name__ == "__main__":
    main(sourcefolder, tknfolder, params)
