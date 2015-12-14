# -*- encoding: utf-8 -*-
# Less lazy dude's version
# Reads the syntactic ngram node file
# these can be gotten from http://bionlp.utu.fi/finnish-internet-parsebank.html
#

import sys
import codecs
import argparse
import gzip
import re

word_re=re.compile(ur"^[a-zA-ZäöåÄÖÅ-]+$",re.U)

if __name__=="__main__":
    parser = argparse.ArgumentParser(description='Filter vocabulary to be indexed')
    parser.add_argument('--counts-per-length', default='0,0,5000,50,2', help='How many times should a known word appear at minimum. Comma separated list of values, one for every word length. 0 means drop. Default %(default)s')
    parser.add_argument('--only-words', default=False, action="store_true", help='Only look for real words, ignore stuff containing weird characters. Default %(default)s')
    args = parser.parse_args()

    length_filter=[int(i) for i in args.counts_per_length.split(",")]
    for line in sys.stdin:
        line=unicode(line.rstrip("\n"),"utf-8")
        form,pos,features,count=line.split("\t")
        count=int(count)
        lf=min(len(form),len(length_filter))
        if length_filter[lf-1]==0 or length_filter[lf-1]>count:
            continue
        if args.only_words and not word_re.match(form):
            continue
        print form.encode("utf-8")

