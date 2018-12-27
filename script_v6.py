import glob
import os
import numpy as np

new_fna_files = glob.glob('*.fna')
for n in new_fna_files:
    pre = n.split('.')[0]
    os.system("mafft --quiet --auto " + str(n) + " > " + str(pre) + ".mafft")
    #os.system("mafft --quiet --auto --clustalout" + str(n) + " > " + str(pre) + "-clustal.mafft")

mafft_files = glob.glob('*.mafft')
for m in mafft_files:
    matrix = []
    ref = []
    with open(m, 'r') as mf:                                                   
        fna_file = mf.read()
        fna_file = fna_file.split('>')
        fna_file.pop(0)                                                         
        for index in range(len(fna_file)):
            fna = fna_file[index]
            fna = fna.split('\n')
            name = fna[0]                                                       
            #genus, id_ = name[:3], name[3:]
            sequence = ''.join(fna[1:])#fna[1]
            ref.append([str(name),str(sequence)])
            sequence = list(sequence)
            array = []
            for s in sequence:
                if s == '-':
                    array.append(1)
                else:
                    array.append(0)
            matrix.append(array)
    if len(matrix) == 1:
        with open(m.split('.')[0] + "-intermediate.fna", 'w') as final:
            for r in ref:    
                final.write('>' + r[0] + '\n')                                  
                final.write(r[1] + '\n') 
        continue
    i = 0
    l = len(matrix[0])
    j = l - 1
    matrix = np.array(matrix)
    right_index = j
    sentinel2 =  False
    while j > 0 and sentinel2 == False:
        candidate = matrix[:,j]
        if (candidate == 0).all() == True:
            right_index = j
            sentinel2 = True
        j = j - 1
    sentinel1 = False
    left_index = i
    while i < l and sentinel1 == False:                                         
        candidate = matrix[:,i]                                                 
        if (candidate == 0).all() == True:
            left_index = i
            sentinel1 = True
        i = i + 1
    new_m = m.split('.')[0]
    with open(new_m + "-intermediate.fna", 'w') as final:
        for r in ref:
            final.write('>' + r[0] + '\n')
            final.write(str(r[1][left_index:right_index+1]) + '\n')
