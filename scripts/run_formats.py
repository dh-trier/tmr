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

import formats0_tagging
import formats1_tkn
import formats2_frq
import formats3_tdm
import formats4_src
import formats5_sel
from os.path import join


# ==================================
# Parameters (need to be set)
# ==================================

lang = "de"
coll = "eb"
seglen = 20000 # segment length
casing = "lower" # "lower"|"original"
token = "mixed" # "lemma"|"pos" ## expand to wordforms
#pos = ["NN0", "NN1", "NN2", "AJ0", "AV0", "VVG", "VVD", "VVN"] # list of POS-tags or "all"
#pos = ["DET:ART", "DET:POS", "PRP", "PRP:det", "PUN", "PRO:PER", "PRO:REL", "PRO:DEM", "KON"] # list of POS-tags or "all"
pos = ["NN", "NE", "ADV", "ADJA", "ADJD", "VVFIN", "VAFIN"]
#pos = "all"

params = {"lang":lang, "coll":coll, "seglen":seglen, "casing":casing, "token":token, "pos":pos}


# ==================================
# Files and folders (don' change)
# ==================================

wdir = join("..")
plainfolder = join(wdir, "source", lang, coll, "plain", "")
taggedfolder = join(wdir, "source", lang, coll, "tagged", "")

tknfolder = join(wdir, "target", lang, coll, "tkn"+"-"+token, "")
frqfolder = join(wdir, "target", lang, coll, "frq"+"-"+casing, "")
tdmfolder = join(wdir, "target", lang, coll, "tdm"+"-"+str(seglen), "")
srcfolder = join(wdir, "target", lang, coll, "src"+"-"+str(seglen), "")
ngrfolder = join(wdir, "target", lang, coll, "sel"+"-"+token, "")


# ==================================
# Call imported scripts
# ==================================

#formats0_tagging.main(plainfolder, taggedfolder, params)
formats1_tkn.main(taggedfolder, tknfolder, params)
#formats2_frq.main(taggedfolder, frqfolder, params)
#formats3_tdm.main(taggedfolder, tdmfolder, params)
#formats4_src.main(taggedfolder, srcfolder, params)
#formats5_sel.main(taggedfolder, ngrfolder, params)
