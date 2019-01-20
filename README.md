# WITOD
A Tool for Within-Taxon Operational Taxonomic Unit (OTU) Diversity

![alt text](https://github.com/johncava/WITOD/blob/master/OTU_Image.png)

# Requirements
1) Python 3.6.4 
2) NCBI BLAST 2.6.0
3) MAFFT 7.402

# Usage

python witod.py -input BUOY_otu_table.txt -out OTU_TABLE_FINAL -rep_set rep_set.fna -silva silva97rep -similarity 0.97<br />
<br />
-input THE FILE NAME OF THE ORIGINAL OTU TABLE TO BE ANALYZED<br />
-out THE NAME OF THE FINAL OTU TABLE OUPUT<br />
-rep_set THE FILE NAME OF THE .FNA FILE OF THE SEQUENCES FOR THE OTU TABLE<br />
-silva THE NAME OF THE SILVA FILES USED FOR BLASTN<br />
-similarity THE SIMILARITY THRESHOLD USED FOR BLASTN<br />
<br />

Developed by: John Kevin Cava <br />
Principal Investigator: Huansheng Cao (Biodesign Center for Fundamental and Applied Microbiomics)
