# Less lazy dude's version
# Reads the syntactic ngram node file
# these can be gotten from http://bionlp.utu.fi/finnish-internet-parsebank.html
#

import sys
import codecs
import argparse
import gzip

counter={} #key: (wform,pos,feat) value:count

if __name__=="__main__":
    parser = argparse.ArgumentParser(description='List vocabulary from the nodes file of syntactic ngrams')
    parser.add_argument('nodesfile', nargs='?', default=("/home/ginter/syntactic-ngram-builder-clean/ngrams_ud/nodes.sorted_by_count.txt.gz",), help='Nodes file. Default %(default)s')
    args = parser.parse_args()

    with gzip.open(args.nodesfile[0],"r") as f:
        for idx,line in enumerate(f):
            line=unicode(line.rstrip("\n"),"utf-8")
            if not line:
                continue
            wform,nodes,count=line.split(u"\t")
            count=int(count)
            nodes=[n for n in nodes.split(u" ") if n.endswith(u"/0")] #pick just the root
            if not (len(nodes)==1 and nodes[0].startswith(wform)):
                print >> sys.stderr, "WTF:", idx, repr(line)
                continue
            #allright, so kill me, I skip everything with / to ease my life
            if u"/" in wform:
                continue
            form,lemma,pos,feat,deprel,head=nodes[0].split(u"/")
            counter[(form,pos,feat)]=counter.get((form,pos,feat),0)+count
            if idx%100000==0:
                print >> sys.stderr, idx, "nodes done"
    #Done, now print that counter
    for ((form,pos,feat),count) in counter.iteritems():
        print (u"\t".join((form,pos,feat,unicode(count)))).encode("utf-8")

