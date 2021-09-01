# -*- coding: utf-8 -*-
"""
Created on Fri Dec  6 13:30:17 2019

@author: jpeng11
"""

import os
abspath = os.path.abspath('C:/Users/jpeng11/coursera/Algorithms for DNA Sequence')
os.chdir(abspath)

# question 1:

def readGenome(filename):
    
    genome = ""
    with open(filename, 'r') as fh:
        for line in fh:
            if not line[0] == '>':
                genome += line.rstrip()
    return genome
    

def globalAlignment(p, t):
    D = []
    for i in range(len(p) +1):
        D.append([0]*(len(t) + 1))
    
    for i in range(len(t) + 1):
        D[0][i] = 0
    for i in range(len(p) + 1):
        D[i][0] = i
    for i in range(1, len(p) + 1):
        for j in range(1, len(t) + 1):
            distHor = D[i][j-1] + 1
            distVec = D[i-1][j] + 1
            if p[i-1] == t[j-1]:
                distDiag = D[i-1][j-1]
            else:
                distDiag = D[i-1][j-1] + 1
            D[i][j] = min(distHor, distVec, distDiag)
        
    return min(D[len(p)])

p = 'ATCG'
t = 'ATCGGGTCTCATC'

genome = readGenome("chr1.GRCh38.excerpt.fasta")
p = 'GCTGATCGATCGTACG'
globalAlignment(p, genome)

p= 'GATTTACCAGATTGAG'
globalAlignment(p, genome)

globalAlignment(p, t)
def readFastq(filename):
    sequences = []
    qualities = []
    with open(filename, 'r') as fh:
        while True:
            fh.readline()
            seq = fh.readline().rstrip()
            fh.readline()
            qual = fh.readline().rstrip()
            if len(seq) == 0:
                break
            sequences.append(seq)
            qualities.append(qual)
           
    return sequences, qualities

reads, _ = readFastq("ERR266411_1.for_asm.fastq")

len(reads)

def overlap(a, b, min_length=3):
    """ Return length of longest suffix of 'a' matching
        a prefix of 'b' that is at least 'min_length'
        characters long.  If no such overlap exists,
        return 0. """
    start = 0  # start all the way at the left
    while True:
        start = a.find(b[:min_length], start)  # look for b's prefix in a
        if start == -1:  # no more occurrences to right
            return 0
        # found occurrence; check for full suffix/prefix match
        if b.startswith(a[start:]):
            return len(a)-start
        start += 1  # move just past previous match
        
 
from itertools import permutations

list(permutations([1,2,3], 2))

def kmer_set(reads, k):
    reads_kmer = {}
    for read in reads:
        kmer = set()
        for i in range(len(read)-k +1):
            kmer.add(read[i:i+k])
        reads_kmer[read] = kmer
    return reads_kmer

reads_kmer = kmer_set(reads, 3)

def naive_overlap_map(reads, k):
    reads = list(set(reads))
    reads_kmers = {}
    for read in reads:
        read_kmer = set()
        for i in range(len(read) - k +1):
            kmer = read[i:i+k]
            read_kmer.add(kmer)
        reads_kmer[read] = read_kmer
    olaps = {}
    for a, b in permutations(reads, 2):
        if a[-k:] not in reads_kmers[b]:
            continue
        olen = overlap(a, b, min_length = k)
        if olen > 0:
            olaps[(a, b)] = olen
    return olaps

reads = ['ACGGATGATC', 'GATCAAGT', 'TTCACGGA']
print(naive_overlap_map(reads, 3))

def kmer_set(reads, k):
    reads_kmer = {}
    for read in reads:
        kmer = set()
        for i in range(len(read)-k +1):
            kmer.add(read[i:i+k])
        reads_kmer[read] = kmer
    return reads_kmer

reads_kmer = kmer_set(reads, 3)
    
def overlap_all_pairs(reads, k):
    reads_kmers = {}
    overlaps = {}
    for read in reads:
        read_kmer = set()
        for i in range(len(read)-k+1):
            kmer = read[i:i+k]
            read_kmer.add(kmer)
        reads_kmers[read] = read_kmer
    for a, b in permutations(reads,2):
        if a[-k:] not in reads_kmers[b]:
            continue
        olen = overlap(a, b, min_length = k)
        if olen > 0:
            overlaps[(a, b)] = olen
    return overlaps
            
reads = ['ABCDEFG', 'EFGHIJ', 'HIJABC']
overlap_all_pairs(reads, 3)
overlap_all_pairs(reads, 4)

reads = ['CGTACG', 'TACGTA', 'GTACGT', 'ACGTAC', 'GTACGA', 'TACGAT']
overlap_all_pairs(reads, 4) 
overlap_all_pairs(reads, 5)

reads, _ = readFastq("ERR266411_1.for_asm.fastq")
overlaps = overlap_all_pairs(reads, 30)
len(overlaps)
len(reads)


print(overlaps[1:10])
print(overlaps[1][1])
uniq_a = set()
for i in range(len(overlaps)):
    a = overlaps[i][0]
    uniq_a.add(a)
uniq_a = list(uniq_a)
    
len(uniq_a)

    
