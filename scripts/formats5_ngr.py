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
        if params["pos"] == "all": 
            features = [token.split("\t")[2] for token in tagged if len(token.split("\t"))== 3]
        else: 
            features = [token.split("\t")[2] for token in tagged if len(token.split("\t"))== 3 and token.split("\t")[1] in params["pos"]]
    if params["token"] == "pos":
        if params["pos"] == "all": 
            features = [token.split("\t")[1] for token in tagged if len(token.split("\t"))==3]
        else: 
            features = [token.split("\t")[1] for token in tagged if len(token.split("\t"))==3 and token.split("\t")[1] in params["pos"]]
    features = "\n".join(features)
    return features


def create_ngrams(features, params): 
    ngrams = zip(*[features[i:] for i in range(params["ngram"])])
    ngrams = [" ".join(ngram) for ngram in ngrams]
    ngrams = "\n".join(ngrams)
    return ngrams


def save_features(features, ngrfolder, filename): 
    filepath = join(ngrfolder, filename+".txt")
    with open(filepath, "w", encoding="utf-8") as outfile:
        outfile.write(features)
    

# ====================================
# MAIN
# ====================================

def main(sourcefolder, ngrfolder, params):
    print("\nformats5_ngr")
    if not os.path.exists(ngrfolder):
        os.makedirs(ngrfolder)
    allcounts = {}
    for textfile in glob.glob(join(sourcefolder, "*.txt")):
        filename = get_filename(textfile)
        print("--"+filename)
        tagged = read_text(textfile)
        features = select_features(tagged, params)
        save_features(features, ngrfolder, filename)
        #ngrams = create_ngrams(features, params)
        #save_features(ngrams, ngrfolder, filename)

if __name__ == "__main__":
    main(sourcefolder, ngrfolder, params)
