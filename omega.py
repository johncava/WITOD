import glob
import os

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
for s in samples_dict.keys():
    with open('./' + s + '/OTU_TABLE_FINAL.txt','r') as f:
        f.readline()
        for line in f:
            line = line.split(',')
            if line[0] not in otu_dict:
                otu_dict[line[0]] = (line[2],line[3],line[4])
            if line[0] not in samples_dict[s]:
                samples_dict[s][line[0]] = line[1]

sample_headers = samples_dict.keys()
print(sample_headers)
for otu in otu_dict.keys():
    output_line = [otu]
    ra = []
    for sa in samples_dict.keys():
        if otu in samples_dict[sa]:
            ra.append(samples_dict[sa][otu])
        else:
            ra.append(str(0.0))
    output_line = output_line + ra + [otu[2],otu[1],otu[0]]
    print(len(output_line))
            
