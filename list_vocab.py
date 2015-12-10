# lazy dude's version -> grab the initial vocabulary from our w2v models
# will do a better job later
#
# these are the files which can be gotten for example from
# http://bionlp.utu.fi/finnish-internet-parsebank.html
#
# Todo: use rather the raw parsebank so we get also frequencies and that kind of stuff
from wvlib import wvlib
import codecs
import sys

# Grabbed this one from wvlib (well I wrote it myself there, so I guess that's not stealing code ;)
# https://github.com/spyysalo/wvlib/blob/master/wvlib.py

def read_word(f):
    wchars=[]
    while True:
        c=f.read(1)
        if c==' ':
            break
        if not c:
            raise ValueError("Whoops. The .bin file ended already?")
        wchars.append(c)
    return unicode(''.join(wchars),"utf-8") #this may also fire few unicode errors

def list_vocab(f, max_rank=None):
    """Read Mikolov's binary w2v format"""
    # terminal newlines are present in word2vec.c output but all
    # versions of released word2vec binary format data, e.g. the
    # GoogleNews-vectors-negative300.bin.gz file available from
    # https://code.google.com/p/word2vec/ . To address the issue,
    # allow newline as the initial character of words and remove
    # it if present.
    wcount,vsize=f.readline().rstrip('\n').split(' ')
    wcount,vsize=int(wcount),int(vsize)
    print >> sys.stderr, "Vocabulary max size:", wcount
    if max_rank is None or max_rank>wcount:
        max_rank=wcount
    for _ in xrange(max_rank): #read exactly max_rank words
        try:
            w=read_word(f).strip()
        except ValueError:
            w=None
            #...must still skip over that vector
        f.read(vsize*4) #skip over the vector which is vsize*4B
        if w:
            print w.lower().encode("utf-8")

if __name__=="__main__":
    with open("/home/ginter/w2v/pb34_wf_200_v2.bin","rb") as f:
        list_vocab(f)

