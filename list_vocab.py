#lazy dude's version -> grab the initial vocabulary from our w2v models
#will do a better job later
from wvlib import wvlib
import codecs
import sys

m=wvlib.load("/home/ginter/w2v/pb34_wf_200_v2.bin",max_rank=500000)
for w in m.words():
    print w.encode("utf-8").lower()

