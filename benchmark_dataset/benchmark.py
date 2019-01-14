import argparse
import os
import glob

###
# Benchmark script to tes tthe fundamental portion of the tool i.e trimming and alignment from OTU Table
###

parser = argparse.ArgumentParser()                                              
                                                                                
parser.add_argument("-input",help= "Input OTU Table file name")                 
parser.add_argument("-out", help= "Output OTU Table file name")                     
parser.add_argument("-rep_set", help= "Rep Set Path")         
                                                                                
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
    os.system("mv checker.py " + WORKING_DIRECTORY)

    os.chdir('./' + WORKING_DIRECTORY)                                                         
                                                                                    
    os.system("python filter_v3.py " + args.rep_set + " " + args.input + " " + str(column))
    print('Stage 1 Complete')
    os.system("python -W ignore otu_filter_1.py")
    print('Stage 2 Complete')                                                
    os.system("python script_v6.py")
    print('Stage 3 Complete')                                                             
    os.system("python post.py")
    print('Stage 4 Complete')                                                                  
    #os.system("python otu_v1.py")
    #print('Stage 5 Complete')                                                                
    #os.system("python -W ignore otu_filter_2.py")
    #print('Stage 6 Complete')
    os.system("python checker.py " + samples[column])                                                                                                                 
                                                                                    
    os.system("mv filter_v3.py ./../")                                                           
    oqs.system("mv otu_filter_1.py ./../")                                                        
    os.system("mv script_v6.py ./../")                                                           
    os.system("mv post.py ./../")                                                                
    os.system("mv otu_v1.py ./../")                                                              
    os.system("mv otu_filter_2.py ./../")                                                        
    os.system("mv checker.py ./../")
    
    # Grab Taxa OTU Number Summary File
    s = glob.glob('*-taxa-count.txt')[0]
    os.system('mv ' + s + ' ./../')

    os.chdir('./../')

# Combine Taxa Summary Counts
os.system('python final-checker.py')
print('Done')
