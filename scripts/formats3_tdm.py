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
#from sklearn.feature_extraction.text import CountVectorizer as cv

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


def create_features(tagged, params):
    if params["casing"] == "lower": 
        features = [item.split("\t")[0].lower()+"_"+item.split("\t")[1]+"_"+item.split("\t")[2] for item in tagged if len(item.split("\t"))==3]
    else:
        features = [item.split("\t")[0]+"_"+item.split("\t")[1]+"_"+item.split("\t")[2] for item in tagged if len(item.split("\t"))==3]
    return features 


def create_segments(features, params): 
    segments = [features[x:x+params["seglen"]] for x in range(0, len(features), params["seglen"])]
    return segments


def clean_tdm(tdm, filename): 
    tdm = tdm.fillna(0).T
    tdm[filename+"_sum"] = np.sum(tdm, axis=1)
    tdm = tdm.sort_values(filename+"_sum", axis=0, ascending=False)
    return tdm
    

def make_tdm(segments, filename):
    """
    Could also be solved more elegantly using CountVectorizer: https://scikit-learn.org/stable/modules/generated/sklearn.feature_extraction.text.CountVectorizer.html
    """
    allseries = []
    counter = 0
    for seg in segments: 
        vector = Counter(seg)
        series = pd.Series(vector, name=filename+"_"+str(counter))
        counter +=1
        allseries.append(series)
    tdm = pd.DataFrame(allseries)
    tdm = clean_tdm(tdm, filename)
    #print(tdm.head())
    return tdm
        

def save_tdm(tdm, targetfolder, filename, params):
    filepath = join(targetfolder, filename+".csv")
    with open(filepath, "w", encoding="utf-8") as outfile:
        tdm.to_csv(outfile, sep="\t")


# ====================================
# MAIN
# ====================================

def main(sourcefolder, targetfolder, params):
    print("\nformats1_tdm")
    if not os.path.exists(targetfolder):
        os.makedirs(targetfolder)
    for textfile in glob.glob(join(sourcefolder, "*.txt")):
        filename = get_filename(textfile)
        print("--"+filename)
        tagged = read_text(textfile).split("\n")
        features = create_features(tagged, params)
        segments = create_segments(features, params)
        tdm = make_tdm(segments, filename)
        save_tdm(tdm, targetfolder, filename, params)

if __name__ == "__main__":
    main(sourcefolder, targetfolder, params)
