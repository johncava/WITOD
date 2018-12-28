#!/bin/bash                                                                     
                                                                                
#SBATCH -n 16                        # number of cores                           
#SBATCH -t 2-12:00                  # wall time (D-HH:MM)                       
#SBATCH -o slurm.%j.out             # STDOUT (%j = JobId)                       
#SBATCH -e slurm.%j.err             # STDERR (%j = JobId)                       
#SBATCH --mail-type=ALL             # Send a notification when the job starts, stops, or fails
#SBATCH --mail-user=jcava@asu.edu # send-to address                             
                                                                                
module load ncbi-blast/2.6.0                                                    
module load python/3.6.4                                                        
module load mafft/7.402

python witod.py -input otu_table-r1_min1000_w_taxa.txt -out OTU_TABLE_FINAL -rep_set rep_set.fna -silva silva97rep -similarity 0.97 -column 20 -dir C20
python witod.py -input otu_table-r1_min1000_w_taxa.txt -out OTU_TABLE_FINAL -rep_set rep_set.fna -silva silva97rep -similarity 0.97 -column 21 -dir C21
python witod.py -input otu_table-r1_min1000_w_taxa.txt -out OTU_TABLE_FINAL -rep_set rep_set.fna -silva silva97rep -similarity 0.97 -column 22 -dir C22
