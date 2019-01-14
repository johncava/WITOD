import glob

taxa = {}
with open('benchmark_expected.txt','r') as expect:
    expect.readline()
    for line in expect:
        line = line.split('\n')[0].split('\t')
        taxa[line[0]] = line[1]

sample_files = glob.glob('*-taxa-count.txt')

sample_dic = {}
for sample in sample_files:
    sample_taxa = {}
    with open(sample, 'r') as s:
        s.readline()
        for line in s:
            line = line.split('\n')[0].split('\t')
            tn = line[0].split('-final')[0]
            #tn = tn.split(';')
            #tn = '_'.join(tn)
            #print(tn)
            sample_taxa[tn] = line[1]
    sample_name = sample.split('-taxa-count.txt')[0]
    sample_dic[sample_name] = sample_taxa

final = []
for t in taxa.keys():
    l = []
    #print(t)
    for sample_ in sample_dic.keys():
        k = t.split(';')
        k = '_'.join(k)
        if k not in sample_dic[sample_].keys():
            l.append('N/A')
            continue
        l.append(str(sample_dic[sample_][k]))
    l = [t] + [str(taxa[t])] + l
    final.append('\t'.join(l))

with open('benchmark_validation.txt','w') as validation:
    header = ['Taxa'] + ['Expected'] + list(sample_dic.keys())
    header = '\t'.join(header)
    validation.write(header + '\n')
    for f in final:
        validation.write(f + '\n')