import glob
import os
import sys

###
# For each *-combined.fna file, blastn the trimmed *-combined.fna files to retrieve
# the associated silva taxon IDs for the sequences
###

silva_rep = sys.argv[1]
files_ = glob.glob('*-combined.fna')
num_threads = int(sys.argv[2])
for file_ in files_:
    temp = file_.split('.fna')[0] + '-16S.silva.blast'
    #print('blastn -db silva97rep -query ' + file_ + ' -out ' + temp + ' -evalue 1e-5 -outfmt 7 -num_threads ' + str(num_threads))
    os.system('blastn -db ./../' + silva_rep +' -query ' + file_ + ' -out ' + temp + ' -evalue 1e-5 -outfmt 7 -num_threads ' + str(num_threads))
