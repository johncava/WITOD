import random
import string

Max_Taxa = 800
Max_OTU = 120
Max_Mutations = 10
Max_Post_Mutations = 10
Max_Sample = 3
seq_length = 200

# Name of rep_set file
rep_set_file = 'rep_set.fna'

# Name of OTU Table
otu_table_file = 'OTU_TABLE.txt'

# Nucleotides
nucleotides = ['A','G','T','C']

# Mutation Function
def mutate(s):
    new_s = ''
    index = None
    n = None
    # Pick Mutation
    m_type = int(random.random()*4)
    if m_type == 0:
        index = random.choice(range(2,len(s)-2))
        new_s = s[:index] + s[index:]
    if m_type == 1:
        index = random.choice(range(2,len(s)-2))
        n = random.choice(nucleotides)
        new_s = s[:index] + str(n) + s[index:]
    if m_type == 2:
        index = random.choice(range(2,len(s)-2))
        new_s = s[:index] + random.choice(nucleotides) + s[index+1:]
    if m_type == 3:
        index = random.choice(range(2,len(s)-2))
        new_s = s[:index] + random.choice(nucleotides) + s[index+1:]
    return new_s

def postmutate(s):
    n = None
    # Pick Mutation
    m_type = int(random.random()*5)
    if m_type == 0:
        n = random.choice(nucleotides)
        s = str(n) + s
    if m_type == 1:
        n = random.choice(nucleotides)
        s = s + str(n)
    return s

# Create Taxa Name
taxa_dic = {1: 'k', 2: 'p', 3:'c', 4:'o', 5:'f', 6:'g', 7:'g'}
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
    numberOTUs = random.choice(range(1,Max_OTU + 1))
    # Add taxa and number of OTUs to benchmark summary
    b_summary.append((taxa_name,numberOTUs))
    # Create sequence
    seq = ''.join(random.choice(nucleotides) for _ in range(seq_length))
    for otu in range(1,numberOTUs):
        # Mutate Sequence
        seq_copy = seq
        for _ in range(Max_Mutations):
            seq_copy = mutate(seq_copy)
        for _ in range(Max_Post_Mutations):
            seq_copy = postmutate(seq_copy)
        fna_sequences.append(('OTU' + str(((taxa - 1)*Max_OTU) + otu), seq_copy))
        s = []
        for sample in range(1, Max_Sample + 1):
            s.append(str(int(random.random()*1000)))
        otu_table.append(['OTU' + str(((taxa - 1)*Max_OTU) + otu)] + s + [taxa_name])

# Write benchmark to summary benchmark txt
with open('benchmark_summary.txt','w') as w:
    w.write('Taxa Name' + '\t' + 'Number Of OTUs\n')
    for item in b_summary:
        w.write(item[0] + '\t' + str(item[1]) + '\n')

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
