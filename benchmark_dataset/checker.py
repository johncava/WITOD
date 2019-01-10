import glob
import sys

# Take all taxa .fna files
files = glob.glob('*.fna')

# Count OTUs per Taxa
taxa_summary = []

for file_ in files:
    # Get Name of Taxa
    file_name = file_.split('.fna')[0]
    numOTUs = 0
    with open(file_, 'r') as f:
        fna_file = f.read()
        fna_file = fna_file.split('>')[1:]
        numOTUs = len(fna_file)
    # Add info to taxa summary
    taxa_summary.append((file_name, numOTUs))

sample_name = sys.argv[1]
# Write taxa otu summary for sample
with open(sample_name +'-taxa-count.txt','w') as w:
    w.write('Taxa Name' + '\t' + 'Number Of OTUs\n')
    for item in taxa_summary:
        w.write(item[0] + '\t' + item[1] + '\n')
