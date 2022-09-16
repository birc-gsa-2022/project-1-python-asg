"""Implementation of a linear time exact matching algorithm."""

################################################################
# libraries:
import sys
import argparse

################################################################
# Functions:

from align import get_edits
from cigar import edits_to_cigar
    
def border_array(x:str):
    if x == '' or x == None:
        return []
    ba = [0]
    j = 0
    for i in range(1,len(x)):
        while x[i] != x[j] and j > 0:
            j = ba[j-1]
        if x[i] == x[j]:
            ba.append(j+1)
            j+=1
        if j == 0:
            ba.append(j)      
    return ba


def strict_border_array(x:str):
    if x == '' or x == None:
        return []
    ba = border_array(x)
    for i in range(len(x)-1):
        if ba[i] > 0 and x[ba[i]] == x[i+1]:
            ba[i] = ba[ba[i]-1]
    return ba


def ba_algorithm(ref:str, read:str):
    if ref == '' or ref == None:
        return []
    if read == '' or read == None:
        return []
    ref=ref.strip().upper()
    read=read.strip().upper()
    if len(read) > len(ref):
        return False
    if len(read) == len(ref):
        return False

    strict_ba_of_read = strict_border_array(read)
    match_positions = []
    j = 0
    for idx in range(len(ref)):
        while read[j] != ref[idx] and j != 0:
            j = strict_ba_of_read[j-1]    
        if ref[idx] == read[j]:
            j+=1
        if j == len(read):
            match_positions.append(idx-len(read)+1)
            j = strict_ba_of_read[j-1]
    return match_positions


def read_fasta():
    # load input:
    inFile = sys.argv[1]
    with open(inFile,'r') as f:
        lines = f.readlines()
    record_list = []
    header = ''
    sequence = []
    for line in lines:
        line = line.strip()
        if line.startswith('>'):
            if header != "":
                record_list.append([header.strip(), ''.join(sequence).strip()])
                sequence = []
            header = line[1:]
        else:
            sequence.append(line)
    record_list.append([header.strip(), ''.join(sequence).strip()])
    return record_list


def read_fastq():
    inFile = sys.argv[2]  
    with open(inFile,'r') as f:
        lines = f.readlines()
    record_list = []
    header = ''
    sequence = []
    for line in lines:
        line = line.strip()
        if line.startswith('@'):
            if header != "":
                record_list.append([header.strip(), ''.join(sequence).strip()])
                sequence = []
            header = line[1:]
        else:
            sequence.append(line)
    record_list.append([header.strip(), ''.join(sequence).strip()])
    return record_list

################################################################
# Code:
    
if __name__ == '__main__':
    
    fasta_recs = read_fasta()
    fastq_recs = read_fastq()
    
    for fq_rec in fastq_recs:
        for fa_rec in fasta_recs:
            matches = ba_algorithm(fa_rec[1], fq_rec[1])
            for match in matches:
                read_name = fq_rec[0]
                read_seq = fq_rec[1]
                edits = get_edits(read_seq, fa_rec[1][match:match+len(fq_rec[1])])
                cigar = edits_to_cigar(edits[2])
                output = [read_name,fa_rec[0],str(match+1),cigar,read_seq]
                print('\t'.join(output))
        
################################################################



