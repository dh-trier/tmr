#!/usr/bin/env python3
# author: #cf, 2020.

"""
Pipeline to create derived formats from an annotated full-text corpus.

Presupposes the existence of an annotated full text in TSV format,
with one token per line and Tab-separated annotations. 

Creates a derived format suitable for applications like stylometric 
text similarity measurement, topic modeling or analysis of distinctive
features. 

"""


# =================================
# Import statements
# =================================

import formats1_tdm
import formats2_src
from os.path import join


# ==================================
# Parameters
# ==================================

seglen = 5000 # segment length
casing = "original" # "lower"|"original"
params = {"seglen":seglen, "casing":casing}


# ==================================
# Files and folders
# ==================================

wdir = join("..")
sourcefolder = join(wdir, "source", "tagged", "")

# formats1_tdm
tdmfolder = join(wdir, "target", "tdm"+"-"+str(seglen), "")

# formats2_src
srcfolder = join(wdir, "target", "src"+"-"+str(seglen), "")

# ==================================
# Call imported scripts
# ==================================

formats1_tdm.main(sourcefolder, tdmfolder, params)
#formats2_src.main(sourcefolder, srcfolder, params)
