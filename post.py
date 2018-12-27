import glob
import os
import numpy as np
files = glob.glob('*-intermediate.fna')                                                
                                                                                
for file_ in files:                                                             
    if file_ in ['PLA-intermediate.fna','LEP-intermediate.fna','PSE-intermediate.fna']:                   
        continue
    with open(file_, 'r') as f:
        fna_file = f.read()
        fna_sequences = fna_file.split('>')[1:]
        # Check for file with one sequence
        if len(fna_sequences) == 1:
            new_name = file_.split('-')[0] + '-final.fna'
            os.system('cp ' + file_ + ' ' + new_name)
            continue
        matrix = []
        storage = []
        for fna in fna_sequences:
            fna = fna.split('\n')
            name, sequence = fna[0], fna[1]
            storage.append([name, sequence])
            matrix.append(list(sequence))
            #print(name,sequence)
        #print('\n')
        matrix = np.array(matrix)
        # Begin comparison
        check = np.all(matrix == matrix[0,:], axis = 0)
        check = check.tolist()
        i = 0
        j = len(check) - 1
        while i < len(check) - 1:
            if (check[i] == True) and (check[i+1] == True):
                break
            i = i + 1
        while j > 0:
            if (check[j] == True) and (check[j-1] == True):
                break
            j = j - 1
        # Save
        final_name = file_.split('-')[0] + '-final.fna'
        with open(final_name, 'w') as w:
            for s in storage:
                w.write('>' + str(s[0]) +'\n')
                w.write(str(s[1][i:j+1]) + '\n')
