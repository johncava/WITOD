import glob
import os
import sys
from scipy.stats import linregress

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

for s in samples_dict.keys():
    with open('./' + s + '/OTU_DIVERSITY.txt','r') as f:
        f.readline()
        # X, Y = Abundance, Number of OTUs
        x,y = [],[]
        for line in f:
            line = line.strip('\n').split(',')
            x.append(float(line[1]))
            y.append(float(line[2]))
        # Compute linear regression
        linear = linregress(x,y)
        samples_dict[s] = [linear.slope, linear.intercept, linear.rvalue]
        
with open('./DIVERSITY_SLOPES.txt','w') as w:
    w.write('Sample, Slope, Intercept, R Value\n')
    for s in samples_dict.keys():
        line = [s] + [str(l) for l in samples_dict[s]]
        line = ','.join(line)
        w.write(line + '\n')

os.system('mkdir diversity')

for s in samples_dict.keys():
    os.system('cp ./' + s + '/OTU_DIVERSITY.txt ./diversity/' + s + '-DIVERSITY.txt')

'''
otu_dict = {}
sample_otu_table_name = sys.argv[2]
for s in samples_dict.keys():
    with open('./' + s + '/' + sample_otu_table_name+'.txt','r') as f:
        f.readline()
        for line in f:
            line = line.split(',')
            if line[0] not in otu_dict:
                otu_dict[line[0]] = (line[2],line[3],line[4])
            if line[0] not in samples_dict[s]:
                samples_dict[s][line[0]] = line[1]

sample_headers = samples_dict.keys()
output_file_name = sys.argv[1]
with open(output_file_name + '.txt','w') as w:
    header = ['OTU ID'] + list(sample_headers) + ['Taxa', 'Silva Taxa ID', 'Sequence']
    w.write(','.join(header) + '\n')
    for otu in otu_dict.keys():
        output_line = [otu]
        ra = []
        for sa in samples_dict.keys():
            if otu in samples_dict[sa]:
                ra.append(samples_dict[sa][otu])
            else:
                ra.append(str(0.0))
        item = otu_dict[otu]
        output_line = output_line + ra + [item[2].split('\n')[0],item[1],item[0]]
        w.write(','.join(output_line) + '\n')
'''
