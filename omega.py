import glob
import os
import sys

# Create file with the sample directories
os.system('ls -d */ > sample_list.txt')

# Read in the sample directory file
sample_dirs = glob.glob('sample_list.txt')[0]
samples = []
samples_dict = {}
with open(sample_dirs,'r') as s:
    for line in s:
        l = line.split('\n')[0].split('/')[0]
        if l == 'benchmark_dataset':
            continue
        samples.append(l)
        samples_dict[l] = {}

otu_dict = {}
sample_otu_table_name = sys.argv[2]
for s in samples_dict.keys():
    with open('./' + s + '/' + sample_otu_table_name+'.txt','r') as f:
        f.readline()
        for line in f:
            line = line.split(',')
            if line[0] not in otu_dict:
                otu_dict[line[0]] = (line[2],line[3],line[4].split('\n')[0])
            if line[0] not in samples_dict[s]:
                samples_dict[s][line[0]] = line[1]

sample_headers = samples_dict.keys()
output_file_name = sys.argv[1]
with open(output_file_name + '.txt','w') as w:
    header = ['OTU ID'] + sample_headers + ['Taxa', 'Silva Taxa ID', 'Sequence']
    w.write(header + '\n')
    for otu in otu_dict.keys():
        output_line = [otu]
        ra = []
        for sa in samples_dict.keys():
            if otu in samples_dict[sa]:
                ra.append(samples_dict[sa][otu])
            else:
                ra.append(str(0.0))
        output_line = output_line + ra + [otu[2],otu[1],otu[0]]
        w.write(output_line + '\n')
            
