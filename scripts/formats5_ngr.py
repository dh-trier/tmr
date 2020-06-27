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
    if params["token"] == "wordform":
        if params["pos"] == "all": 
            features = [token.split("\t")[0].lower() for token in tagged if len(token.split("\t"))==3]
        else: 
            features = [token.split("\t")[0].lower() for token in tagged if len(token.split("\t"))==3 and token.split("\t")[1] in params["pos"]]
    return features


def create_ngrams(ngrams, params): 
    ngrams = zip(*[ngrams[i:] for i in range(params["ngram"])])
    ngrams = [" ".join(ngram) for ngram in ngrams]
    return ngrams


def save_features(ngrams, ngrfolder, filename): 
    ngrams = "\n".join(ngrams)
    filepath = join(ngrfolder, filename+".txt")
    with open(filepath, "w", encoding="utf-8") as outfile:
        outfile.write(ngrams)



def count_allngrams(allngrams):
    from collections import Counter
    allcounts = dict(Counter(allngrams))
    filteredcounts = dict()
    for (key, value) in allcounts.items():
        if value > 5:
            filteredcounts[key] = value
    print(filteredcounts)
    return filteredcounts


def save_counts(counts, ngrfolder): 
    counts = pd.Series(counts)
    counts.sort_values(ascending=False, inplace=True)
    print(counts.head(20))
    with open(join(ngrfolder, "allngrs.tsv"), "w", encoding="utf8") as outfile: 
        counts.to_csv(outfile, sep="\t")
    

    

# ====================================
# MAIN
# ====================================

def main(taggedfolder, ngrfolder, params):
    print("\nformats5_ngr")
    if not os.path.exists(ngrfolder):
        os.makedirs(ngrfolder)
    allcounts = {}
    allngrams = []
    for textfile in glob.glob(join(taggedfolder, "*.txt")):
        filename = get_filename(textfile)
        print("--"+filename)
        tagged = read_text(textfile)
        features = select_features(tagged, params)
        ngrams = create_ngrams(features, params)
        allngrams.extend(ngrams)
        save_features(ngrams, ngrfolder, filename)
    filteredcounts = count_allngrams(allngrams)
    save_counts(filteredcounts, ngrfolder)


if __name__ == "__main__":
    main(taggedfolder, ngrfolder, params)
