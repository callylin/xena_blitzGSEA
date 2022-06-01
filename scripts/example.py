import blitzgsea as blitz
import urllib.request
import pandas as pd

def run_blitz():
	# download example gene expression signature
	url = "https://github.com/MaayanLab/blitzgsea/raw/main/testing/ageing_muscle_gtex.tsv"
	urllib.request.urlretrieve(url, "ageing_muscle_gtex.tsv")
	
	# read signature as pandas dataframe
	signature = pd.read_csv("ageing_muscle_gtex.tsv")

	# use enrichr submodule to retrieve gene set library
	library = blitz.enrichr.get_library("KEGG_2021_Human")
	print(library)
	
	# run enrichment analysis
	# pd.set_option('display.max_rows', None)
	# result = blitz.gsea(signature, library)

	# plot the enrichment results and save to pdf
	fig = blitz.plot.running_sum(signature, "CELL ADHESION MOLECULES", library, result = result, compact=False)
	fig.savefig("running_sum.png", bbox_inches = 'tight')

	# fig_compact = blitz.plot.running_sum(signature, "CELL ADHESION MOLECULES", library, result = result, compact = True)
	# fig_compact.savefig("running_sum_compact.png", bbox_inches = 'tight')

	# fig_table = blitz.plot.top_table(signature, library, result, n = 50)
	# fig_table.savefig("top_table.png", bbox_inches = 'tight')
	
if __name__ == '__main__':
	run_blitz()
