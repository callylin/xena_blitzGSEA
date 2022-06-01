import  blitzgsea as blitz
import pandas as pd
import argparse

def commandLineArgs(): 
        '''function takes in names of output files'''
        parser = argparse.ArgumentParser()
        parser.add_argument('--fullTableFile', '-f', type = str, action = 'store', help = 'output file for full table')
        parser.add_argument('--topTableFile', '-t', type = str, action = 'store', help = 'output file for top table')
        args = parser.parse_args()
        fullFile = args.fullTableFile
        topFile = args.topTableFile
        
        return fullFile, topFile # full table (.tsv), top table (.png) - returns the two file names

def reformat_gmt(file):
        '''reformats data from geneset library file into dictionary'''
        genesetDict = {}
        with open(file) as gmt:
                for line in gmt:
                        gene = line.split()
                        del gene[1]
                        genesetDict[gene[0]] = [gene[1]]
                        for item in range(2, len(gene)):
                                genesetDict[gene[0]].append(gene[item])
        return genesetDict

def reformat_rnk(file):
        '''reformats data from signature file into pandas dataframe'''
        signatureList = []
        with open(file) as rnk:
                for line in rnk:
                        geneList = []
                        gene = line.split()
                        geneList.append(gene[0])
                        geneList.append(float(gene[1]))
                        signatureList.append(geneList)
        signatureDF = pd.DataFrame(signatureList, columns = ['0', '1'])
        return signatureDF

def runBlitz(signature, library):
        ''' function that runs blitzGSEA and collects result in pandas dataframe'''
        # run enrichment analysis
        pd.set_option('display.max_rows', None)
        result = blitz.gsea(signature, library)

        # plot top table
        topTable = blitz.plot.top_table(signature, library, result, n = 50)

        return result, topTable # returns pandas dataframe and top table

def main():
        arguments = commandLineArgs()
        library = reformat_gmt('c2_c3.gmt')
        signature = reformat_rnk('ESR1_low_versus_ESR1_high.rnk')
        data = runBlitz(signature, library)
        fullTable = data[0]
        topTable = data[1]
        fullTable.to_csv(arguments[0], sep = "\t") # write dataframe to .tsv file
        topTable.savefig(arguments[1], bbox_inches = 'tight') # save top table to .png file

if __name__ == '__main__':
        main()