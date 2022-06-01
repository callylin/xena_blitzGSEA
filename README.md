## Project Overview
Gene set enrichment analysis (GSEA) is a computational method that is commonly used by researchers and scientists to determine whether there is an association between a set of genes and disease phenotype [1]. GSEA-P, GSEApy, and fGSEA are all different GSEA implementations. Recently, a group of researchers at Ma’ayan Labs developed blitzGSEA. The algorithm is claimed to have “significant improvement in performance.” [2] Before implementing blitzGSEA into Xena for users to run, the results produced must be confirmed to make biological sense, and the runtime and memory usage of the algorithm is established to be efficient. The functionalities of blitzGSEA were tested and ran with several files; each analysis was not only completed efficiently but also produced results that were logical when compared to those produced through traditional GSEA. 
## Objective
The Xena Browser is utilized by many scientists and researchers to visualize cancer genomics,  so it is critical that results are accurate and efficiently computed. To ensure this, over the span of 10 weeks, the project consisted of: 
* Understanding the results produced from blitzGSEA and implementing a full table result and detailed output 
* Testing and evaluating the results produced from blitzGSEA to determine if it is biologically sound
* Determining the runtime and memory usage of running blitzGSEA with GNU time
* Investigating the Enrichr libraries 
