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
                                                                                
args = parser.parse_args()

sample_otu_table_name = "SAMPLE_OTU_TABLE"
otu_file = args.input
numColumns = None
samples = None
with open(otu_file, 'r') as f:
    samples = f.readline().split('\t')
    numColumns = len(samples)

##########
# For Loop for each Sample
for column in range(1,numColumns - 1):

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
                                                                                    
    os.system("python filter_v3.py " + args.rep_set + " " + args.input + " " + str(column))
    print('Stage 1 Complete')
    os.system("python -W ignore otu_filter_1.py")
    print('Stage 2 Complete')                                                
    os.system("python script_v6.py")
    print('Stage 3 Complete')                                                             
    os.system("python post.py")
    print('Stage 4 Complete')                                                                  
    os.system("python otu_v1.py")
    print('Stage 5 Complete')                                                                
    os.system("python -W ignore otu_filter_2.py")
    print('Stage 6 Complete')                                                
    os.system("python blast.py " + args.silva)
    print('Stage 7 Complete')                                                                 
    os.system("python otu_silva_v4.py " + sample_otu_table_name + " " + args.similarity)
    print('Stage 8 Complete')                                                          
    os.system("python final.py")
    print('Stage 9 Complete')
    os.system("python diversity_v2.py " + sample_otu_table_name)
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

    os.chdir('./../')
###############
os.system("python omega.py " + args.out + " " + sample_otu_table_name)
os.system("python diversity-overview.py " + "FINAL_SAMPLE_DIVERSITY " + "OTU_DIVERSITY")
print('Done')
