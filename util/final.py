import glob
import os

###
# Creates the .mafft files from the .fna files outputted from the tool
###

files_ = glob.glob('*-combined-16S.silva.fna')

for file_ in files_:
    mafft_file = file_.split('.fna')[0] + '.mafft'
    os.system('mafft --auto --quiet --clustalout ' + file_ + ' > ' + mafft_file)
