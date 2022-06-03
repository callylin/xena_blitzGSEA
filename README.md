## Project Overview
Gene set enrichment analysis (GSEA) is a computational method that is commonly used by researchers and scientists to determine whether there is an association between a set of genes and disease phenotype [1]. GSEA-P, GSEApy, and fGSEA are all different GSEA implementations. Recently, a group of researchers at Ma’ayan Labs developed blitzGSEA. The algorithm is claimed to have “significant improvement in performance.” [2] Before implementing blitzGSEA into Xena for users to run, the results produced must be confirmed to make biological sense, and the runtime and memory usage of the algorithm is established to be efficient. The functionalities of blitzGSEA were tested and ran with several files; each analysis was not only completed efficiently but also produced results that were logical when compared to those produced through traditional GSEA. 
## Objective
The Xena Browser is utilized by many scientists and researchers to visualize cancer genomics,  so it is critical that results are accurate and efficiently computed. To ensure this, over the span of 10 weeks, the project consisted of: 
* Understanding the results produced from blitzGSEA and implementing a full table result and detailed output 
* Testing and evaluating the results produced from blitzGSEA to determine if it is biologically sound
* Determining the runtime and memory usage of running blitzGSEA with GNU time
* Investigating the Enrichr libraries 

## Results & Outcomes
Throughout the 10 weeks, a better understanding of blitzGSEA was gained and several scripts were written to utilize the functionalities available. It was determined that the Pandas dataframe returned from blitzGSEA could be used to provide users with a full table result in a .tsv format which includes the enrichment score (ES), normalized enrichment score (NES), and other data for every geneset of their library—as seen [here](https://github.com/callylin/xena_blitzGSEA/tree/main/results). In addition, the functions written within the source code were found to be able to be used to provide individuals with specific details of a geneset of their choosing along with a top table and running sum plot; an example can be found [here](https://github.com/callylin/xena_blitzGSEA/tree/main/results/detailed_output). A final [main script](https://github.com/callylin/xena_blitzGSEA/blob/main/scripts/main.py) was written, combining the functions that generate the full-table and detailed results. It takes in two .tsv files (a geneset library and signature) and reformats it to the proper form for blitzGSEA to run.

The main script was used to run analysis on 2 differential gene expression signatures and 3 geneset libraries—resulting in a total of 6 analyses. When running the analyses for the first time, several NES values were being computed as -inf/inf which was unexpected. After further research, it was found that the way the blitzGSEA source code was calculating the values had to be rewritten accordingly to produce a finite value. It is unknown why the rearranging of equations results in the proper value, but the analyses were rerun after the code was modified (modified code available [here](https://github.com/callylin/blitzgsea)). 

As seen in Table 1, each analysis was completed within a reasonable amount of time (user time < 150 seconds) and memory usage (< 950 megabytes). The results computed by blitzGSEA were compared to previous results from traditional GSEA, and several scatter plots were made between the NES values to verify the validity of the values produced by blitzGSEA. Each scatter plot between all positive and negative NES’ from both blitzGSEA and traditional GSEA had a correlation coefficient (r) > than 0.78 which is an indication of high accuracy (Table 1 & Figure 1). 

| Signature (.rnk) | Geneset (.gmt) | Size | Time (s) | Memory (mb) | r |
|      :----:      |     :----:     | :---:|  :----:  |   :----:    |:-:|
| basal_versus_lum |      c2_c3     | 7494 | 121.28 | 303.968 | 0.78891888 |
| basal_versus_lum | c5.all.v7.5.1.symbols | 15473 | 119.78 | 477.532 | — |
| basal_versus_lum | msigdb.v7.5.1.symbols | 32880 | 144.36 | 994.368 | - |
| ESR1_low_versus_ESR1_high |      c2_c3     | 7494 | 116.80 | 308.456 | 0.88312513 |
| ESR1_low_versus_ESR1_high | c5.all.v7.5.1.symbols | 15473 | 118.71 | 444.304 | 0.87125943 |
| ESR1_low_versus_ESR1_high | msigdb.v7.5.1.symbols | 32880 | 144.95 | 939.568 |0.88575674 |

## References
[1] Subramanian, A., Tamayo, P., Mootha, V. K., Mukherjee, S., Ebert, B. L., Gillette, M. A., Paulovich, A., Pomeroy, S. L., Golub, T. R., Lander, E. S., & Mesirov, J. P. (2005). Gene set enrichment analysis: a knowledge-based approach for interpreting genome-wide expression profiles. Proceedings of the National Academy of Sciences of the United States of America, 102(43), 15545–15550. https://doi.org/10.1073/pnas.0506580102 

[2] Lachmann, A., Xie, Z., & Ma'ayan, A. (2022). blitzGSEA: Efficient computation of Gene Set Enrichment Analysis through Gamma distribution approximation. Bioinformatics (Oxford, England), btac076. Advance online publication. https://doi.org/10.1093/bioinformatics/btac076 
