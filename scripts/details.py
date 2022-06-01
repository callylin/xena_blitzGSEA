import  blitzgsea as blitz
import urllib.request
import pandas as pd
import numpy as np
import argparse

def commandLineArgs():
    ''' function takes in names of output files'''
    parser = argparse.ArgumentParser()
    parser.add_argument('--detailFile', '-d', type = str, action = 'store', help = 'detailed output file')
    parser.add_argument('--plotFile', '-p', type = str, action = 'store', help = 'file for plot')
    args = parser.parse_args()
    detailedOutputFile = args.detailFile
    runningPlotFile = args.plotFile
        
    return detailedOutputFile, runningPlotFile # detailed table (.tsv), running sum plot (.png)

def detailedOutput(signature, geneset, library):
    signatureMap = {} # holds rank of genes?
    detailsDict = {} # dictionary for data for each gene in geneset

    signature = signature.sort_values(1, ascending = False).set_index(0)
    signature = signature[~signature.index.duplicated(keep = 'first')]
    for i, h in enumerate(signature.index): # iterate through signature file and add gene name as dict key, # (rank) as dict value
        signatureMap[h] = i

    geneset = library[geneset] # geneset holds all gene names from specific geneset 
    runningSum, es = blitz.enrichment_score(np.array(np.abs(signature.iloc[:,0])), signatureMap, geneset)
    runningSum = list(runningSum)

    leadingEdge = blitz.get_leading_edge(runningSum, signature, geneset, signatureMap)

    for i, x in enumerate(signature.index): # iterate through signature file
        if x in geneset: # if gene in signature file AND in geneset, add gene name as dict key, # (rank) as a dict value in list
            detailsDict[x] = [i]

    for key in detailsDict.keys(): # iterate through keys in dict
        value = signature.loc[key][1] # get rank metric value from signature file, and add to key's value list 
        detailsDict[key].append(value) 
        detailsDict[key].append(runningSum[detailsDict[key][0]]) # get running ES from running sum list and, and add to key's value list 
        if key in leadingEdge:
            detailsDict[key].append("Yes")
        else:
            detailsDict[key].append("No")

    '''create pandas data frame with data'''
    data = pd.DataFrame.from_dict(detailsDict, orient = 'index') # convert dictionary to pandas dataframe
    data.columns = ["Rank in Gene List", "Rank Metric Score", "Running ES", "Leading Edge"]

    return data # return pandas dataframe

def runBlitz(geneset):
    ''' function that runs blitzGSEA, gets detailed output, and plots graph'''

    # download example gene expression signature
    url = "https://github.com/MaayanLab/blitzgsea/raw/main/testing/ageing_muscle_gtex.tsv"
    urllib.request.urlretrieve(url, "ageing_muscle_gtex.tsv")

    # read signature as pandas dataframe
    signature = pd.read_csv("ageing_muscle_gtex.tsv")

    # use enrichr submodule to retrieve gene set library
    library = blitz.enrichr.get_library("KEGG_2021_Human")

    # run enrichment analysis
    result = blitz.gsea(signature, library)

    # detailed output
    data = detailedOutput(signature, geneset, library)

    # plot running sum (non-compact)
    figure = blitz.plot.running_sum(signature, geneset, library, result = result, compact = False)

    return data, figure # return pandas dataframe and plot

def main():
    arguments = commandLineArgs()
    geneset = input("Please enter the geneset you would like to run blitzGSEA on: ")
    returned = runBlitz(geneset)
    detailedOutputFile = returned[0]
    plot = returned[1]
    detailedOutputFile.to_csv(arguments[0], sep = "\t") # write dataframe to .tsv file
    plot.savefig(arguments[1], bbox_inches = 'tight') # save running sum plot to .png file

if __name__ == '__main__':
    main()