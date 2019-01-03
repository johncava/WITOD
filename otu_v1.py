import glob

###
# Takes the *-final.fna files and combines identical sequences together
###

files = glob.glob('*-final.fna')

for file_ in files:
    if file_ in ['PLA-fina.fna','LEP-final.fna','PSE-final']:
        continue
    with open(file_,'r') as f:
        fna_file = f.read()
        fna_sequences = fna_file.split('>')[1:]
        #print('Total Number: ' + str(len(fna_sequences)))
        sequences = []
        map_ = []
        for fna in fna_sequences:
            fna = fna.split('\n')
            #print(fna[0],fna[1])
            sequences.append(fna[1])
            map_.append((fna[0],fna[1]))
        seq_set = set(sequences)
        seq_dic = {}
        for s in list(seq_set):
            seq_dic[s] = []
            for item in map_:
                if s == item[1]:
                    seq_dic[s].append(item[0])
        name = file_.split('-')[0]
        # Create the fasta file
        with open(name + '-combined.fna','w') as w:
            for key in seq_dic.keys():
                combined_name = ''
                for n in seq_dic[key]:
                    combined_name = combined_name + str(n) + '_'
                combined_name = combined_name.strip('_')
                w.write('>' + combined_name + '\n')
                w.write(str(key) + '\n')
    #print('\n')
