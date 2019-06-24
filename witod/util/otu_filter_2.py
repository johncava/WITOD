import glob
import os

###
# Moves all *-combined.fna files that only have one OTU to otu_filter_2 folder
###

os.system('mkdir otu_filter_2')
files_ = glob.glob('*-combined.fna')
for file_ in files_:
    check = False
    with open(file_,'r') as f:
        fna_file = f.read()
        fna_file = fna_file.split('>')[1:]
        if len(fna_file) <= 1:
            check = True
    if check:
        os.system('mv ' + file_ + ' otu_filter_2')

