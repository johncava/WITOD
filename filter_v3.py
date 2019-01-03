import glob                                                                     
import sys


###
# First script that takes the original OTU table and the rep_set.fna file to create *.fna files
# associated with a specific taxon. 
### 

# Load rep_set.fna                                                              
dic = {}                                                                        
repset_file = sys.argv[1]
with open('./../' + repset_file,'r') as fn:
    fna_files = fn.read()                                                       
    fna_files = fna_files.split('>')[1:]                                        
    for fna_file in fna_files:                                                  
        fna = fna_file.split('\n')                                              
        name, seq = fna[0].split(' ')[0], fna[1]                                
        dic[name] = seq

otu_table_file = sys.argv[2]
column = int(sys.argv[3])
with open('./../'+otu_table_file, 'r') as f:
    data = []
    for line in f:                                                              
        data.append(line.split('\t'))                                           
    # Remove headers                                                            
    data.pop(0)
    # Retrieve column of interest                                               
    columns = data.pop(0)
    # Select Relative abundance, OTU ID, and Taxa based on column of interest   
    for index_interest in range(column, column + 1):
        subset = []
        for d in data:
            subset.append((d[0],float(d[index_interest]),d[-1].strip('\n')))
        sum_ = sum([item[1] for item in subset])
        new_subset = []
        for s in subset:
            new_subset.append((s[0],s[1]/sum_,s[2]))
        final = new_subset
        taxa_set = []
        lis = []
        for f in final:
            # If abundance is zero
            if f[1] == 0:
                continue
            # If taxa is undefined
            taxa = f[-1].split(';')
            if taxa == ['U',' n',' a',' s',' s',' i',' g',' n',' e',' d']:
                continue
            taxa = [t.split('__')[-1] for t in taxa]
            taxa = [t for t in taxa if t is not '']
            # If taxa information is only Kingdom and Phylum
            if len(taxa) <= 2:
                continue
            taxa_set.append('_'.join(taxa))
            new_id = f[0]
            if 'New.Reference' in new_id:
                new_id = new_id.split('New.Reference')[-1]
            if 'New.CleanUp.Reference' in new_id:
                new_id = 'Clean' + new_id.split('New.CleanUp.Reference')[-1] 
            # New_ID, Taxa, Sequence, Relative_Abundance
            lis.append((new_id,'_'.join(taxa),dic[f[0]], f[1]))
        taxa_set = set(taxa_set)
        for s in taxa_set:
            if len(glob.glob(s + '.fna')) > 0:
                continue
            with open('./' + s + '.fna','w') as w:
                for l in lis:
                    if s == l[1]:
                        w.write('>' + l[0] + '\n')
                        w.write(l[2] + '\n')
        with open('./' + str(columns[index_interest]) + '-relative_abundance.txt', 'w') as ra:
            ra.write('ID, Relative Abundance'+ '\n')
            for r in lis:
                ra.write(r[0] + ' ' + str(r[3]) +' \n')
