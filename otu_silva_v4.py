import glob
import os
import sys

###
# Creates the sample OTU Table for each sample column of the original OTU table
###

files_ = glob.glob('*.blast')

combined = glob.glob('*-combined.fna')

abundance_files = glob.glob('*-relative_abundance.txt')

# Create Abundance Dictionary                                                   
otu_dic = {}
def get_cumm(string, file_name):
    t_dic = {}
    with open(file_name,'r') as a:
        a.readline()
        for line in a:
            line = line.split(' ')
            name, relative = line[0], float(line[1])
            t_dic[name] = relative                                              
    relative_abundance = []
    for s in string.split('_'):
        if s not in t_dic:
            relative_abundance.append(0.0)
        else:
            relative_abundance.append(t_dic[s])
    cumm_abundance = sum(relative_abundance)
    return cumm_abundance
        
for c in combined:                                                            
    with open(c,'r') as f:                                                  
        fna_file = f.read()                                                     
        fna_file = fna_file.split('>')[1:]                                      
        for fna in fna_file:                                                    
            fna = fna.split('\n')                                               
            name, seq = fna[0], fna[1]                                          
            #print(name,seq)
            otu_dic[name] = seq

finalize = []
similarity = float(sys.argv[2])
for file_ in files_:
    # Create ID Set
    id_set = []
    dic = {}
    with open(file_,'r') as f:
        array = []
        for line in f:
            if line.startswith('#'):
                continue
            l = line.strip('\n').split('\t')
            #print(l)
            #l[2] = float(l[2])
            array.append(tuple(l))
            id_set.append(l[0])
    id_set = list(set(id_set))
    # Initialize Dictionary
    for i in id_set:
        dic[i] = []
    for a in array:
        if a[0] in id_set:
            dic[a[0]].append(a)
    #finalize = []
    finalize_fna = []
    for key in dic.keys():
        copy = dic[key]
        check = copy[0]
        if float(check[2]) < similarity:
            continue
        new_taxa = [check[1]]
        #end = 1
        #iteration = 0
        for i,v in enumerate(copy):
            if i == 0:
                continue
            if ((v[2] == check[2]) and (v[3] == check[3]) and (v[10] == check[10]) and (float(v[2]) >= similarity)) == True:
                new_taxa.append(v[1])
            else:
                break
        cumm_array = []
        for rel in abundance_files:
           cumm = get_cumm(key,rel)
           cumm_array.append(str(cumm))    
        finalize.append([key] + cumm_array + [str(otu_dic[key]).upper()] + [str('_'.join(new_taxa))] + [str(file_.split('-combined')[0])])
        finalize_fna.append(['_'.join(new_taxa), otu_dic[key]])
    finalize_name = file_.split('.blast')[0] + '.fna'   
    with open(finalize_name, 'w') as fw:
        for final in finalize_fna:
            fw.write('>' + final[0] +'\n')
            fw.write(final[1] + '\n')

output_otu_table_name =  sys.argv[1]
with open(output_otu_table_name + '.txt', 'w') as write:
    sample_names = [sample.split('-relative_abundance.txt')[0] for sample in abundance_files]
    sample_names = ','.join(sample_names)
    write.write('OTU ID,' + sample_names + ',SEQ, SILVA ID, TAXA' +'\n')
    for final in finalize:
        write.write(','.join(final) + '\n')
