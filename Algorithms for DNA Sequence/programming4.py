# -*- coding: utf-8 -*-
"""
Created on Mon Dec  9 16:07:57 2019

@author: jpeng11
"""

import os
abspath = os.path.abspath('C:/Users/jpeng11/coursera/Algorithms for DNA Sequence')
os.chdir(abspath)

def overlap(a, b, min_length=3):
    """ Return length of longest suffix of 'a' matching
        a prefix of 'b' that is at least 'min_length'
        characters long.  If no such overlap exists,
        return 0. """
    start = 0  # start all the way at the left
    while True:
        start = a.find(b[:min_length], start)  # look for b's suffx in a
        if start == -1:  # no more occurrences to right
            return 0
        # found occurrence; check for full suffix/prefix match
        if b.startswith(a[start:]):
            return len(a)-start
        start += 1  # move just past previous match

import itertools

def scs(ss):
    """ Returns shortest common superstring of given
        strings, which must be the same length """
    shortest_sup = None
    for ssperm in itertools.permutations(ss):
        sup = ssperm[0]  # superstring starts as first string
        for i in range(len(ss)-1):
            # overlap adjacent strings A and B in the permutation
            olen = overlap(ssperm[i], ssperm[i+1], min_length=1)
            # add non-overlapping portion of B to superstring
            sup += ssperm[i+1][olen:]
        if shortest_sup is None or len(sup) < len(shortest_sup):
            shortest_sup = sup  # found shorter superstring
    return shortest_sup  # return shortest

ss = ['CCT', 'CTT', 'TGC', 'TGG', 'GAT', 'ATT']

def scs_multiple(ss):
    """ Returns all possible shortest common superstring of given
        strings, which must be the same length """
    shortest_sups = []
    for ssperm in itertools.permutations(ss):
        shortest_sup = None
        sup = ssperm[0]  # superstring starts as first string
        for i in range(len(ss)-1):
            # overlap adjacent strings A and B in the permutation
            olen = overlap(ssperm[i], ssperm[i+1], min_length=1)
            # add non-overlapping portion of B to superstring
            sup += ssperm[i+1][olen:]
        if shortest_sup is None or len(sup) < len(shortest_sup):
            shortest_sup = sup  # found shorter superstring
        shortest_sups.append(shortest_sup)
    return shortest_sups  # return shortest
shortest_sups = scs_multiple(ss)

shortest_sups_len = {}
for s in shortest_sups:
    shortest_sups_len 

shortest_len = [len(shortest_sups[i]) for i in range(len(shortest_sups))]
min(shortest_len)
shortest_len.count(11)

from itertools import permutations

def pick_maximal_overlap(reads, k):
    reads = list(set(reads))
    reads_kmers = {}
    for read in reads:
        read_kmer = set()
        for i in range(len(read)-k+1):
            kmer = read[i:i+k]
            read_kmer.add(kmer)
        reads_kmers[read] = read_kmer
    reada, readb = None, None
    best_olen = 0
    for a, b in permutations(reads, 2):
        if a[-k:] not in reads_kmers[b]:
            continue
        
        olen = overlap(a, b, min_length = k)
        if olen > best_olen:
            best_olen = olen
            reada, readb = a, b
    return reada, readb, best_olen

def greedy_scs(reads, k):
    read_a, read_b, olen = pick_maximal_overlap(reads, k)
    while olen > 0:
        reads.remove(read_a)
        reads.remove(read_b)
        reads.append(read_a + read_b[olen:])
        read_a, read_b, olen = pick_maximal_overlap(reads, k)
    return ''.join(reads)


    
def build_kmers(reads, k):
    reads_kmers = {}
    for read in reads:
        read_kmer = set()
        for i in range(len(read) - k + 1):
            read_kmer.add(read[i:i+k])
        reads_kmers[read] = read_kmer
    return reads_kmers


            
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

reads, _ = readFastq("ads1_week4_reads.fq")

assemble = greedy_scs(reads, 5)
print(len(assemble))
        
# 
def greedy_assemble(reads, n):
    reads = list(set(reads))
    reads_kmers = build_kmers(reads, n)
    olen_pairs = {}
    for a, b in permutations(reads, 2):
        if a[-n:] not in reads_kmers[b]:
            continue
        olen = overlap(a, b, min_length = n)
        if olen > n:
            olen_pairs[(a, b)] = olen
    
    while max(olen_pairs.values()) >= n:
        best_pair, best_olen = max(olen_pairs.items(), 
                                   key = lambda k: olen_pairs[k])
        reada = best_pair[0]
        readb = best_pair[1]
        reads.remove(reada)
        reads.remove(readb)
        merged = reada + readb[best_olen:]
        pop_list = []
        for key in olen_pairs.keys():
            if key[0] == reada or key[1] == readb:
                pop_list.append(key)
        for read in reads:
            if merged[-n:] in reads_kmers[read]:
                left_merge = overlap(merged, read, min_length = n)
            if read[-n:] in reads_kmers[merged]:
                right_merge = overlap(read, merged, min_length = n)
            if left_merge >= right_merge:
                olen_pairs[(merged, read)] = left_merge
            else:
                olen_pairs[(read, merged)] = right_merge
                
            left_merge = overlap
        
        
        
olen_pairs = greedy_assemble(reads, 50)
olen_pairs.keys()
olen_pairs.values()
import operator
       
stats = {'a':1000, 'b':3000, 'c': 100, 'd':3000}
max(stats.items(), key = operator.itemgetter(1))[0]
max(stats.values())