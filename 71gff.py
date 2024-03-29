# 71gff.py

# Write a program that converts genes in gff into JSON
# Use the minaturized version of the C. elegans genome (included) this time
# Organize the genes onto chromosomes
# Print the number of genes on each chromosome to stderr
# Your code should mimic the output below

# Hint: your outer data structure is a dictionary

# Note: gene names are stored differently here than the last file

import gzip
import sys
import re
import json

genes = {}



with gzip.open(sys.argv[1], 'rt') as fp:

	while True:
		line = fp.readline()
		if line == '': break
		if not re.search('\\tgene\\t', line): continue
		chr = re.search('\w+', line)[0]
		if chr not in genes: genes[chr] = []
		match = re.search('(\\d+)\\t(\\d+)\\t.\\t(\W)\\t.\\t\S+Alias=(\w+)', line)
		gene = {}
		gene['gene'] = match[4]
		gene['beg'] = int(match[1])
		gene['end'] = int(match[2])
		gene['strand'] = match[3]
		genes[chr].append(gene)
	
	for chr, gene in genes.items(): print(chr, len(gene))
	print(json.dumps(genes, indent=4))
"""
python3 71gff.py elegans
I 37
II 57
III 37
IV 41
MtDNA 2
V 41
X 45
{
    "I": [
        {
            "gene": "Y74C9A.6",
            "beg": 3747,
            "end": 3909,
            "strand": "-"
        },
        {
            "gene": "Y74C9A.3",
            "beg": 4116,
            "end": 10230,
            "strand": "-"
        },
...
"""
