# WITOD
A Tool for Within-Taxon Operational Taxonomic Unit (OTU) Diversity

![alt text](https://github.com/johncava/WITOD/blob/master/OTU_Image.png)

# Requirements
1) Python 3.6.4
2) Scipy 1.3.0
3) Numpy 1.16.4
4) NCBI BLAST 2.6.0
5) MAFFT 7.402

# Usage

Please copy the OTU Table and the rep_set.fna file into the same directory of witod.py and util directory.

/- WITOD <br />
&nbsp;  /- witod <br />
&nbsp;&nbsp;&nbsp;    /- BUOY_otu_table.txt <br />
&nbsp;&nbsp;&nbsp;    /- rep_set.fna <br />
&nbsp;&nbsp;&nbsp;   /- witod.py <br />
&nbsp;&nbsp;&nbsp;    /- util/ <br />

python3 witod.py -input <i>BUOY_otu_table.txt</i> -out <i>OTU_TABLE_FINAL</i> -rep_set <i>rep_set.fna</i> -silva <i>./util/silva97rep</i> -similarity <i>0.97</i> -n <i>8</i><br />

<br />
-input <b>THE FILE NAME OF THE ORIGINAL OTU TABLE TO BE ANALYZED</b><br />
-out <b>THE NAME OF THE FINAL OTU TABLE OUPUT</b><br />
-rep_set <b>THE FILE NAME OF THE .FNA FILE OF THE SEQUENCES FOR THE OTU TABLE</b><br />
-silva <b>THE NAME OF THE SILVA FILES USED FOR BLASTN</b><br />
-similarity <b>THE SIMILARITY THRESHOLD USED FOR BLASTN</b><br />
-n <b>NUMBER OF THREADS FOR BLAST</b><br />
<br />

Developed by: John Kevin Cava <br />
Principal Investigator: Huansheng Cao (Biodesign Center for Fundamental and Applied Microbiomics)
