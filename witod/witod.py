import argparse
import os
import glob

###
# All python scripts called in this script are done in accordance for a specific column (sample) from the original OTU Table.
# This is in order to segregate and make sure that sequences associated in one sample aren't considered in another sample if it isn't there.
###

parser = argparse.ArgumentParser()                                              
                                                                                
parser.add_argument("-input",help= "Input OTU Table file name")                 
parser.add_argument("-out", help= "Output OTU Table file name")                 
parser.add_argument("-silva", help= "Silva Database name")                      
parser.add_argument("-rep_set", help= "Rep Set Path")
parser.add_argument("-similarity", help="Silva Similarity Percentage")         
parser.add_argument("-n", help="number of cores for blast")                                                                                
args = parser.parse_args()

sample_otu_table_name = "SAMPLE_OTU_TABLE"
otu_file = args.input
numColumns = None
samples = None
with open(otu_file, 'r') as f:
    samples = f.readline().split('\t')
    numColumns = len(samples)

os.system("mv ./util/filter_v3.py ./")                                            
os.system("mv ./util/otu_filter_1.py ./")                                         
os.system("mv ./util/script_v6.py ./")                                            
os.system("mv ./util/post.py ./")                                                 
os.system("mv ./util/otu_v1.py ./")                                               
os.system("mv ./util/otu_filter_2.py ./")                                         
os.system("mv ./util/blast.py ./")                                                
os.system("mv ./util/otu_silva_v4.py ./")                                         
os.system("mv ./util/final.py ./")                                
os.system("mv ./util/diversity_v2.py ./")

##########
# For Loop for each Sample
for column in range(1,numColumns - 1):
    
    print('--------------')
    print(samples[column])

    WORKING_DIRECTORY="./" + samples[column]
                                                                                    
    os.system("mkdir " + WORKING_DIRECTORY)                                                      
    os.system("mv filter_v3.py "+ WORKING_DIRECTORY)                                            
    os.system("mv otu_filter_1.py " + WORKING_DIRECTORY)                                         
    os.system("mv script_v6.py "+ WORKING_DIRECTORY)                                            
    os.system("mv post.py "+ WORKING_DIRECTORY)                                                 
    os.system("mv otu_v1.py "+ WORKING_DIRECTORY)                                               
    os.system("mv otu_filter_2.py "+ WORKING_DIRECTORY)                                         
    os.system("mv blast.py " + WORKING_DIRECTORY)                                                
    os.system("mv otu_silva_v4.py "+ WORKING_DIRECTORY)                                         
    os.system("mv final.py "+ WORKING_DIRECTORY)
    os.system("mv diversity_v2.py "+ WORKING_DIRECTORY)
                                         
    os.chdir('./' + WORKING_DIRECTORY)                                                         
                                                                                    
    os.system("python3 -W ignore filter_v3.py " + args.rep_set + " " + args.input + " " + str(column))
    print('Stage 1 Complete')
    os.system("python3 -W ignore otu_filter_1.py")
    print('Stage 2 Complete')                                                
    os.system("python3 -W ignore script_v6.py")
    print('Stage 3 Complete')                                                             
    os.system("python3 post.py")
    print('Stage 4 Complete')                                                                  
    os.system("python3 otu_v1.py")
    print('Stage 5 Complete')                                                                
    os.system("python3 -W ignore otu_filter_2.py")
    print('Stage 6 Complete')                                                
    os.system("python3 -W ignore blast.py " + args.silva + " " + args.n)
    print('Stage 7 Complete')                                                                 
    os.system("python3 otu_silva_v4.py " + sample_otu_table_name + " " + args.similarity)
    print('Stage 8 Complete')                                                          
    os.system("python3 final.py")
    print('Stage 9 Complete')
    os.system("python3 diversity_v2.py " + sample_otu_table_name)
    print('Stage 10 Complete')

    os.system("mv filter_v3.py ./../")                                                           
    os.system("mv otu_filter_1.py ./../")                                                        
    os.system("mv script_v6.py ./../")                                                           
    os.system("mv post.py ./../")                                                                
    os.system("mv otu_v1.py ./../")                                                              
    os.system("mv otu_filter_2.py ./../")                                                        
    os.system("mv blast.py ./../")                                                               
    os.system("mv otu_silva_v4.py ./../")                                                        
    os.system("mv final.py ./../")
    os.system("mv diversity_v2.py ./../")

    os.system("rm *.fna")
    os.system("rm *.mafft")
    os.system("rm *.blast")
    os.system("rm -r otu_filter_1/")
    os.system("rm -r otu_filter_2/")

    os.chdir('./../')

###############
os.system("mv ./util/omega.py ./")
os.system("mv ./util/diversity-overview.py ./")
os.system("mv ./util/calculate-slope.py ./")
os.system("python3 omega.py " + args.out + " " + sample_otu_table_name)
os.system("python3 diversity-overview.py " + "FINAL_SAMPLE_DIVERSITY " + "OTU_DIVERSITY")
os.system('python3 calculate-slope.py')
os.system("mv *.py util/")
os.system("mv util/witod.py ./")
os.system("rm sample_list.txt")
print('Done')
