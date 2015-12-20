'''
Created on December 18, 2015
Description: This module will combine multiple vcf file with same headers
@author: Ronak H Shah
'''
'''
::Input::
vcfFiles : List of VCF Files to combine in list data structure
mergedVCF: Name of the combined vcf to output

::Output::
It is a merged vcf file 
'''
import sys
import vcf
import logging

def run(vcfFiles,combinedVCF,verbose):
	vcf_header = vcf.Reader(filename=vcfFiles[1])
	vcf_output = vcf.Writer(combinedVCF,vcf_header)
	for vcffile in vcfFiles:
		vcf_reader = vcf.Reader(open(vcffile, 'r'))
		for each in vcf_reader:
			vcf_output.write_record(each)
	if(verbose):
		logging.info("Finished combining vcf files")		
	return(combinedVCF)