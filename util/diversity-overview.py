import glob
import os
import sys

###
# Creates the Final Diversity Table from the sample OTU tables created
###

# Create file with the sample directories
#os.system('ls -d */ > sample_list.txt')

# Read in the sample directory file
sample_dirs = glob.glob('sample_list.txt')[0]
samples = []
samples_dict = {}
with open(sample_dirs,'r') as s:
    for line in s:
        l = line.split('\n')[0].split('/')[0]
        if l == 'benchmark_dataset':
            continue
        if l == 'util':
            continue
        samples.append(l)
        samples_dict[l] = {}

taxa_dict = {}
sample_diversity_name = sys.argv[2]
for s in samples_dict.keys():
    with open('./' + s + '/' + sample_diversity_name+'.txt','r') as f:
        f.readline()
        for line in f:
            line = line.strip('\n').split(',')
            if line[0] not in taxa_dict:
                taxa_dict[line[0]] = line[2]
            if line[0] not in samples_dict[s]:
                samples_dict[s][line[0]] = line[2]

sample_headers = samples_dict.keys()
output_file_name = sys.argv[1]
with open(output_file_name + '.txt','w') as w:
    header = ['Taxa'] + list(sample_headers)
    w.write(','.join(header) + '\n')
    for tax in taxa_dict.keys():
        output_line = [tax]
        num_otus = []
        for sa in samples_dict.keys():
            if tax in samples_dict[sa]:
                num_otus.append(samples_dict[sa][tax])
            else:
                num_otus.append(str(0))
        output_line = output_line + num_otus
        w.write(','.join(output_line) + '\n')
            
