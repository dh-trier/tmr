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
    if params["casing"] == "lower": 
        features = [token.split("\t")[0].lower() for token in tagged]
    else: 
        features = [token.split("\t")[0] for token in tagged]
    return features


def get_counts(features): 
    counts = pd.Series(Counter(features))
    counts.sort_values(inplace=True, ascending=False)
    return counts


def save_counts(counts, frqfolder, filename): 
    filepath = join(frqfolder, filename+".txt")
    with open(filepath, "w", encoding="utf-8") as outfile:
        counts.to_csv(outfile, sep="\t")


def save_allcounts(allcounts, frqfolder, params): 
    allcounts = pd.DataFrame(allcounts).fillna(0)
    allcounts["sum"] = np.sum(allcounts, axis=1)
    allcounts.sort_values(by="sum", ascending=False, inplace=True)
    filepath = join(frqfolder, "..", "frq"+"-"+params["casing"]+".csv")
    with open(filepath, "w", encoding="utf-8") as outfile:
        allcounts.to_csv(outfile, sep="\t")
    

# ====================================
# MAIN
# ====================================

def main(sourcefolder, frqfolder, params):
    print("\nformats0_frq")
    if not os.path.exists(frqfolder):
        os.makedirs(frqfolder)
    allcounts = {}
    for textfile in glob.glob(join(sourcefolder, "*.txt")):
        filename = get_filename(textfile)
        print("--"+filename)
        tagged = read_text(textfile)
        features = select_features(tagged, params)
        counts = get_counts(features)
        save_counts(counts, frqfolder, filename)
        allcounts[filename] = counts
    save_allcounts(allcounts, frqfolder, params)

if __name__ == "__main__":
    main(sourcefolder, frqfolder, params)
