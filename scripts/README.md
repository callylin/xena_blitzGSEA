## Scripts
### example.py 
This example.py script was taken from the blitzGSEA GitHub and slightly modified, so it could run with no issues and be used for original testing. It takes in a .tsv file from the blitzGSEA GitHub and retrieves a geneset library from Enrichr. 

### full_table.py
A geneset library (in .gmt) and signature (in .rnk) file is reformatted to a dictionary and pandas dataframe, respectively. blitzGSEA is ran, and the returned pandas dataframe is written into a .tsv file. The .tsv file and a top table is saved to the user's directory. 

* Command-line Arguments: 
  * [\-f]    output file for the full-table
  * [\-t]    output file for the top table

### details.py
Similarily to full_table.py, a geneset library (in .gmt) and signature (in .rnk) file is reformatted to a dictionary and pandas dataframe, respectively. A pandas dataframe is then created with each geneset's name, rank, rank metric score, running enrichment score, and their leading edges after determination of their values. The dataframe is returned as a .tsv file along with a running sum plot of a geneset. 

* Command-line Arguments: 
  * [\-d]    output file for the detailed output of a geneset  
  * [\-p]    output file for running sum plot of a geneset

### main.py
This main.py script takes in 3 input from the user: the file name for the geneset library (.gmt), the file name for the signature (.rnk), and the geneset name they'd like the detailed output and running sum plot be produced for. The files are reformatted accordingly, and blitzGSEA is ran to acquire the information for each geneset. A full-table, detailed output, top table, and running sum plot is outputted to the user's directory. 

* Command-line Arguments: 
  * [\-f]    output file for the full-table
  * [\-d]    output file for the detailed output of a geneset  
  * [\-t]    output file for the top table
  * [\-p]    output file for running sum plot of a geneset
