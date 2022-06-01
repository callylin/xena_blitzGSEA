import sys
sys.path.insert(0, "/Users/callylin/Documents/blitzGSEA/example/blitzgsea")
import  blitzgsea as blitz
import pandas as pd
import numpy as np
import argparse

def commandLineArgs():
        ''' function takes in names of output files'''
        parser = argparse.ArgumentParser()
        parser.add_argument('--fullTableFile', '-f', type = str, action = 'store', help = 'output file for full table')
        parser.add_argument('--detailFile', '-d', type = str, action = 'store', help = 'output file for detailed output')
        parser.add_argument('--topTableFile', '-t', type = str, action = 'store', help = 'output file for top table')
        parser.add_argument('--plotFile', '-p', type = str, action = 'store', help = 'output file for running sum plot')
        args = parser.parse_args()
        fullFile = args.fullTableFile
        detailedOutputFile = args.detailFile
        topFile = args.topTableFile
        runningPlotFile = args.plotFile

        return fullFile, detailedOutputFile, topFile, runningPlotFile # full table (.tsv), detailed table (.tsv), top table (.png), running sum plot (.png)

def reformat_gmt(file):
        '''function reformats a .gmt file to a dictionary'''
        genesetDict = {} 
        with open(file) as gmt: # opens file and reads each line
                for line in gmt: 
                        gene = line.split() # splits the line into a list 
                        del gene[1] # delete element with index 1 (http website)
                        genesetDict[gene[0]] = [gene[1]] # create key and value, then iterate through the rest of the list and append the gene into the value list
                        for item in range(2, len(gene)):
                                genesetDict[gene[0]].append(gene[item])
        return genesetDict # return geneset dictionary

def reformat_rnk(file):
        '''function reformats a .rnk file to a pandas dataframe'''
        signatureList = []
        with open(file) as rnk: # opens file and reads each line
                for line in rnk:
                    geneList = []
                    gene = line.split() # splits the line into a list 
                    if ((float(gene[1]) > 0) or (float(gene[1]) < 0)):
                        geneList.append(gene[0]) # append gene name and its value into gene_list
                        geneList.append(float(gene[1]))
                        signatureList.append(geneList) # append gene_list into signature_list
        signature_df = pd.DataFrame(signatureList, columns = [0, 1]) # create pandas dataframe from list
        pd.set_option('display.max_rows', None)
        
        return signature_df # return signature pandas dataframe 

def detailedOutput(signature, geneset, library, leadingEdges):
        signatureMap = {} # holds rank of genes?
        detailsDict = {} # dictionary for data for each gene in geneset

        signature = signature.sort_values(1, ascending = False).set_index(0)
        signature = signature[~signature.index.duplicated(keep = 'first')]
        for i, h in enumerate(signature.index): # iterate through signature file and add gene name as dict key, # (rank) as dict value
                signatureMap[h] = i

        geneset = library[geneset] # geneset holds all gene names from specific geneset 
        runningSum, es = blitz.enrichment_score(np.array(np.abs(signature.iloc[:,0])), signatureMap, geneset)
        runningSum = list(runningSum)

        for i, x in enumerate(signature.index): # iterate through signature file
                if x in geneset: # if gene in signature file AND in geneset, add gene name as dict key, # (rank) as a dict value in list
                        detailsDict[x] = [i]

        for key in detailsDict.keys(): # iterate through keys in dict
                value = signature.loc[key][1] # get rank metric value from signature file, and add to key's value list 
                detailsDict[key].append(value)
                detailsDict[key].append(runningSum[detailsDict[key][0]]) # get running ES from running sum list and, and add to key's value list 
                if key in leadingEdges:
                        detailsDict[key].append("Yes")
                else:
                        detailsDict[key].append("No")

        '''create pandas data frame with data'''
        data = pd.DataFrame.from_dict(detailsDict, orient = 'index') # convert dictionary to pandas dataframe
        data.columns = ["Rank in Gene List", "Rank Metric Score", "Running ES", "Leading Edge"]

        return data # return pandas dataframe

def runBlitz(signature, library, geneset):
        ''' function that runs blitzGSEA and collects result in pandas dataframe'''

        # run enrichment analysis
        pd.set_option('display.max_rows', None)
        result = blitz.gsea(signature, library)

        leadingEdges = list(leadingEdges.split(','))

        # detailed output
        details = detailedOutput(signature, geneset, library, leadingEdges)

        # plot top table
        topTable = blitz.plot.top_table(signature, library, result, n = 50)

        # plot running sum (non-compact)
        figure = blitz.plot.running_sum(signature, geneset, library, result = result, compact = False)

        return result, details, topTable, figure # return pandas dataframes, top table, and figure

def main():
        arguments = commandLineArgs()
        libraryInput = input("Please enter the filename (.gmt) for the geneset library: ")
        signatureInput = input("Please enter the filename (.rnk) for the gene signature: ")
        geneset = input("Please enter the geneset you would like to have the detailed output & figure produced for: ")
        library = reformat_gmt(libraryInput)
        signature = reformat_rnk(signatureInput)
        data = runBlitz(signature, library, geneset)

        fullTable = data[0]
        details = data[1]
        topTable = data[2]
        runningSum = data[3]
        fullTable.to_csv(arguments[0], sep = "\t") # write dataframe to .tsv file
        details.to_csv(arguments[1], sep = "\t") # write dataframe to .tsv file
        topTable.savefig(arguments[2], bbox_inches = 'tight') # save top table to .png file
        runningSum.savefig(arguments[3], bbox_inches = 'tight') # save running sum plot to .png file

if __name__ == '__main__':
        main()