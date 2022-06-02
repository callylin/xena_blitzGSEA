## Scripts
#### example.py 
This example.py script was taken from the blitzGSEA GitHub and slightly modified, so it could run with no issues and be used for original testing. It takes in a .tsv file from the blitzGSEA GitHub and retrieves a geneset library from Enrichr. 

#### full_table.py


#### details.py
Similarily to full_table.py, a geneset library (in .gmt) and signature (in .rnk) file is rewritten to a dictionary and pandas dataframe, respectively. A pandas dataframe is then created with each geneset's name, rank, rank metric score, running enrichment score, and their leading edges after determination of their values. The dataframe is returned as a .tsv file along with a running sum plot for a specific geneset. 

* Command-line Arguements: 
  * \-d    output file for the detailed output for a geneset  
* 

#### main.py
