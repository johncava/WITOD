#!/bin/bash                                                                     
                                                                                
#SBATCH -n 16                        # number of cores                           
#SBATCH -t 2-12:00                  # wall time (D-HH:MM)                       
#SBATCH -o slurm.%j.out             # STDOUT (%j = JobId)                       
#SBATCH -e slurm.%j.err             # STDERR (%j = JobId)                       
#SBATCH --mail-type=ALL             # Send a notification when the job starts, stops, or fails
#SBATCH --mail-user=jcava@asu.edu # send-to address

module load python/3.6.4                                                        
module load mafft/7.402

python benchmark.py -input OTU_TABLE.txt -out SAMPLE_OTU_TABLE -rep_set rep_set.fna