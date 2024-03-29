# 70gff.py

# Write a program that converts genes in gff into JSON
# Use the E. coli genome gff
# Your code should mimic the output below
import gzip
import sys
import re
import json

genes = []

with gzip.open(sys.argv[1], 'rt') as fp:

	while True:
		line = fp.readline()
		if line.startswith('###'): break
		if not re.search('ID=gene', line): continue
		gene = {}
		match = re.search('(\\d+)\\t(\\d+)\\t.\\t(\W)\\t\S\\t\S+gene=(\w+)', line)
		gene['gene'] = match[4]
		gene['beg'] = int(match[1])
		gene['end'] = int(match[2])
		gene['strand'] = match[3]
		genes.append(gene)
		
	print(json.dumps(genes, indent=4))


"""
python3 70gff.py ~/DATA/E.coli/GCF_000005845.2_ASM584v2_genomic.gff.gz
[
    {
        "gene": "thrL",
        "beg": 190,
        "end": 255,
        "strand": "+"
    },
    {
        "gene": "thrA",
        "beg": 337,
        "end": 2799,
        "strand": "+"
    },
...
"""
