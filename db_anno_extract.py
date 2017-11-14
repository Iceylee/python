
#!/usr/bin/python

# coding=utf-8

#python db_anno_extract.py [gene-anno-file] [blast-out-file][output-name]

import sys,re

input_file1 = open(sys.argv[1])#"uniprot_sprot.anno"
input_file2 = open(sys.argv[2])#"swissprot.bestHits"
output_file = open(sys.argv[3],"w")#"swissprot.anno.out"

pro_anno = {}
for line in input_file1:
    i1 = line.split(" ")[0][1:]
    i_list = (line.strip()).split(" ")[1:]
    i2 = (" ").join(i_list)
    pro_anno[i1] = i2
    
    
for line in input_file2:
    index = line.split()[1]
    anno = pro_anno[index]
    output_file.write(line.strip() + "\t" + anno + "\n")
    
    
    