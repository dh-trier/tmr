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

import formats1_tkn
import formats2_frq
import formats3_tdm
import formats4_src
import formats5_sel
from os.path import join


# ==================================
# Parameters
# ==================================

seglen = 5000 # segment length
casing = "lower" # "lower"|"original"
token = "lemma" # "lemma"|"pos" ## expand to wordforms
pos = ["NOM", "ADJ", "ADV", "VER:infi", "VER:pper", "VER:pres", "VER:simp", "VER:impf", "VER:impe"] # list of POS-tags or "all"
#pos = ["DET:ART", "DET:POS", "PRP", "PRP:det", "PUN", "PRO:PER", "PRO:REL", "PRO:DEM", "KON"] # list of POS-tags or "all"
#pos = "all"
params = {"seglen":seglen, "casing":casing, "token":token, "pos":pos}


# ==================================
# Files and folders
# ==================================

wdir = join("..")
sourcefolder = join(wdir, "source", "tagged", "")

tknfolder = join(wdir, "target", "tkn"+"-"+token, "")
frqfolder = join(wdir, "target", "frq"+"-"+casing, "")
tdmfolder = join(wdir, "target", "tdm"+"-"+str(seglen), "")
srcfolder = join(wdir, "target", "src"+"-"+str(seglen), "")
ngrfolder = join(wdir, "target", "sel"+"-"+token, "")


# ==================================
# Call imported scripts
# ==================================

#formats1_tkn.main(sourcefolder, tknfolder, params)
#formats2_frq.main(sourcefolder, frqfolder, params)
#formats3_tdm.main(sourcefolder, tdmfolder, params)
#formats4_src.main(sourcefolder, srcfolder, params)
formats5_sel.main(sourcefolder, ngrfolder, params)
