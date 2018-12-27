import glob
import numpy as np

file_ = glob.glob('OTU_TABLE_FINAL.txt')[0]

header = ''
dic = {}
with open(file_,'r') as f:
    header = f.readline()
    for line in f:
        line = line.split(',')
        taxa = line[-1].split('\n')[0]
        if taxa not in dic:
            dic[taxa] = []
        ra_samples = line[1:-3]
        ra_samples = [float(ra) for ra in ra_samples]
        ra_samples = np.array(ra_samples)
        dic[taxa].append(ra_samples)
    
with open('OTU_DIVERSITY.txt','w') as w:
    header = header.split(',')
    taxa_head = header[-1].split('\n')[0]
    samples = ','.join(header[1:-3])
    w.write(taxa_head + "," + samples + "," + "Number Of Unique OTUs" + "\n")
    for key in dic.keys():
        num = len(dic[key])
        abundance = sum(dic[key]).tolist()
        abundance = [str(a) for a in abundance]
        array = [key] + abundance + [str(num)]
        w.write(','.join(array) + '\n')
