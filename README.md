## Project Overview
Gene set enrichment analysis (GSEA) is a computational method that is commonly used by researchers and scientists to determine whether there is an association between a set of genes and disease phenotype [1]. GSEA-P, GSEApy, and fGSEA are all different GSEA implementations. Recently, a group of researchers at Ma’ayan Labs developed blitzGSEA. The algorithm is claimed to have “significant improvement in performance.” [2] Before implementing blitzGSEA into Xena for users to run, the results produced must be confirmed to make biological sense, and the runtime and memory usage of the algorithm is established to be efficient. The functionalities of blitzGSEA were tested and ran with several files; each analysis was not only completed efficiently but also produced results that were logical when compared to those produced through traditional GSEA. 
## Objective
The Xena Browser is utilized by many scientists and researchers to visualize cancer genomics,  so it is critical that results are accurate and efficiently computed. To ensure this, over the span of 10 weeks, the project consisted of: 
* Understanding the results produced from blitzGSEA and implementing a full table result and detailed output 
* Testing and evaluating the results produced from blitzGSEA to determine if it is biologically sound
* Determining the runtime and memory usage of running blitzGSEA with GNU time
* Investigating the Enrichr libraries 
## References
[1] Subramanian, A., Tamayo, P., Mootha, V. K., Mukherjee, S., Ebert, B. L., Gillette, M. A., Paulovich, A., Pomeroy, S. L., Golub, T. R., Lander, E. S., & Mesirov, J. P. (2005). Gene set enrichment analysis: a knowledge-based approach for interpreting genome-wide expression profiles. Proceedings of the National Academy of Sciences of the United States of America, 102(43), 15545–15550. https://doi.org/10.1073/pnas.0506580102 

[2] Lachmann, A., Xie, Z., & Ma'ayan, A. (2022). blitzGSEA: Efficient computation of Gene Set Enrichment Analysis through Gamma distribution approximation. Bioinformatics (Oxford, England), btac076. Advance online publication. https://doi.org/10.1093/bioinformatics/btac076 
