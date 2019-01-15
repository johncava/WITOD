import random
import string
import numpy

Max_Taxa = 300
Max_OTU = 30
Max_Sample = 3
seq_length = 200

# Name of rep_set file
rep_set_file = 'rep_set.fna'

# Name of OTU Table
otu_table_file = 'OTU_TABLE.txt'

# Nucleotides
nucleotides = ['A','G','T','C']

# Mutation Function
def mutate(seq, nOTUs):
    for n in range(nOTUs):
        seq_matrix.append(seq)
    seq_matrix = np.matrix(seq_matrix)

    num_combine = random.choice([1,2,3,4,5])
    mutate = nucleotides.copy()
    mutate.remove(seq[2])
    combined_nucleotide = random.choice(mutate)
    seq_matrix[:num_combine,2] = combined_nucleotide
    k = 3
    for i in range(num_combine,nOTUs):
        mutate = nucleotides.copy()
        mutate.remove(seq[k])
        seq_matrix[i,k] = random.choice(mutate)
        k += 1

    seq_matrix = seq_matrix.tolist()
    for i,v in enumerate(seq_matrix):
        seq_matrix[i] = ''.join(v)

    # Add nucleotides to each sequence to mimic gaps
    for i,s in enumerate(seq_matrix):
        for _ in range(random.choice([0,1,2,3,4,5])):
            flank = random.choice([0,1])
            if flank == 0:
                seq_matrix[i] = random.choice(nucleotides) + s
            elif flank == 1:
                seq_matrix[i] = s + random.choice(nucleotides)

    expected = Max_OTU - num_combine + 1
    return seq_matrix, expected

# Create Taxa Name
taxa_dic = {1: 'k', 2: 'p', 3:'c', 4:'o', 5:'f', 6:'g', 7:'s'}
def create_taxa():
    length = random.choice(range(3,8))
    taxa_name = ';'.join([taxa_dic[i + 1] + '_' + ''.join([random.choice(string.ascii_uppercase + string.digits) for _ in range(4)]) for i in range(length)])
    return taxa_name

fna_sequences = []
otu_table = []
b_summary = []
# For taxa
for taxa in range(1,Max_Taxa + 1):
    # Create Taxa Name
    taxa_name = create_taxa()
    # Randomly choose number of OTUs
    numberOTUs = random.choice(range(7,Max_OTU + 1))
    # Create sequence
    seq = ''.join(random.choice(nucleotides) for _ in range(seq_length))
    seq_list, expected = mutate(seq,numberOTUs)
    # Add taxa and number of OTUs to benchmark summary
    b_summary.append((taxa_name,numberOTUs,expected))
    for i, otu in enumerate(seq_list):
        fna_sequences.append(('OTU' + str(((taxa - 1)*Max_OTU) + i), seq_copy))
        s = []
        for sample in range(1, Max_Sample + 1):
            s.append(str(int((random.random()*1000) + 1)))
        otu_table.append(['OTU' + str(((taxa - 1)*Max_OTU) + i)] + s + [taxa_name])

# Write benchmark to summary benchmark txt
with open('benchmark_summary.txt','w') as w:
    w.write('Taxa Name' + '\t' + 'Number Of OTUs'+ '\t' + 'Expected' + '\n')
    for item in b_summary:
        w.write(item[0] + '\t' + str(item[1]) + '\t' + str(item[2]) + '\n')

# Write expected benchmark
with open('benchmark_expected.txt', 'w') as w:
    w.write('Taxa Name' + '\t' + 'Number Of OTUs' + '\t' + 'Expected' +'\n')
    for item in b_summary:
        if item[1] <= 1:
            continue
        w.write(item[0] + '\t' + str(item[1]) + '\t' + str(item[2]) + '\n')

# Write OTU Sequences to rep_set.fna
with open(rep_set_file,'w') as rep_write:
    for rp in fna_sequences:
        rep_write.write('>' + rp[0] +' \n')
        rep_write.write(rp[1] +'\n')

# Write OTU Table
with open(otu_table_file,'w') as otu_write:
    sample_headers = [str('Sample' + str(x)) for x in range(1,Max_Sample + 1)]
    header = ['OTU ID'] + sample_headers + ['Taxa']
    header = '\t'.join(header)
    otu_write.write(header + '\n')
    for row in otu_table:
        otu_write.write('\t'.join(row) + '\n')