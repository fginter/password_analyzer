#python list_vocab_nodes.py | gzip > all_vocab.txt.gz

rm -f simdb/*.simdb simdb/*.cdb
zcat all_vocab.gz | python filter_vocab.py --only --counts=0,0,10000,1000,100 | simstring -b -d simdb/pb34_wf_exc.simdb -u -s overlap
