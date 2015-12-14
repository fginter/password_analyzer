import simstring
import argparse
import codecs
import sys
import json

out8=codecs.getwriter("utf-8")(sys.stdout)

def match(pwd,vocabdb):
    pwd_lower=pwd.lower()
    matches=[unicode(m,"utf-8") for m in vocabdb.retrieve(pwd_lower.encode("utf-8"))]
    #Quick first try - only use exact hits
    matches=list(set(matches))
    matches=[m for m in matches if m in pwd_lower]
    print >> out8, pwd+u"\t"+json.dumps(matches)

if __name__=="__main__":
    parser=argparse.ArgumentParser(description='Look up using a ready-made web-crawled vocabulary. Pipe the passwords in on stdin.')
    parser.add_argument('--db', default="simdb/pb34_wf_exc.simdb", help='SimString DB built using index_vocab.sh Default: %(default)s')
    args=parser.parse_args()
    vocabdb=simstring.reader(args.db)
    vocabdb.measure=simstring.overlap
    vocabdb.threshold=1.0

    decode_errors=0
    for counter,pwd in enumerate(sys.stdin):
        pwd=pwd.strip()
        if not pwd:
            continue
        try: #there's some broken utf there?
            pwd_u=unicode(pwd,"utf-8")
        except UnicodeDecodeError:
            decode_errors+=1
            continue
        matches=match(pwd_u,vocabdb)
