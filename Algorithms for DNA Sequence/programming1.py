# -*- coding: utf-8 -*-
"""
Created on Tue Nov 26 16:22:41 2019

@author: jpeng11
"""
import os
abspath = os.path.abspath('C:/Users/jpeng11/coursera/Algorithms for DNA Sequence')
os.chdir(abspath)
import wget


url = 'https://d28rh4a8wq0iu5.cloudfront.net/ads1/data/lambda_virus.fa'

wget.download(url, 'lambda_virus.fa')

filename = "lambda_virus.fa"


def readGenome(filename):
    
    genome = ""
    with open(filename, 'r') as fh:
        for line in fh:
            if not line[0] == '>':
                genome += line.rstrip()
    return genome
    
genome = readGenome('lambda_virus.fa')


# question1: count occurence of "ACCT" in both strand

def naive(p, t):
    occurences = []
    for i in range(len(t)-len(p) + 1):
        match = True
        for j in range(len(p)):
            if t[i+j] != p[j]:
                match = False
                break
        if match:
            occurences.append(i)
    return occurences

# read fastq file and return sequences and base quality 
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

def reverseComplement(s):
    complement = {'A':'T', 'C':'G', 'G':'C', 'T':'A', 'N':'N'}
    t = ''
    for base in s:
        t = complement[base] + t
    return t

def naive_with_rc(p, t):
    occurrences = naive(p, t)
    p_comp = reverseComplement(p)
    if p != p_comp:
        occurrence_comp = naive(p_comp, t)
        occurrences.extend(occurrence_comp)
    return occurrences

  

p = "AGGT"
occurrences = naive_with_rc(p, genome)
print("# of occurrence is %d:" % len(occurrences))
      
p = "TTAA"
occurrences = naive_with_rc(p, genome)
print("# of occurrenceis %d:" % len(occurrences))
      
p = "AGTCGA"
occurrences = naive_with_rc(p, genome)
occurrences = sorted(occurrences)

     
p = "ACTAAGT"
occurrences = naive_with_rc(p, genome)
occurrences = sorted(occurrences)
print("# of occurrenceis %d:" % len(occurrences))
      
def naive_2mm(p, t):
    occurrences = []
    for i in range(len(t) - len(p) + 1):
        mismatch_num = 0
        for j in range(len(p)):
            if t[i+j] != p[j]:
                mismatch_num += 1
                if mismatch_num > 2:
                    break
        if mismatch_num < 3:
            occurrences.append(i)
    return occurrences

naive_2mm('ACTTTA', 'ACTTACTTGATAAAGT')

p = 'TTCAAGCC'
occurrences = naive_2mm(p, genome)
print("# of occurrence is %d:" % len(occurrences))
    
p = 'AGGAGGTT'
occurrences = naive_2mm(p, genome)
print("# of occurrence is %d:" % len(occurrences))
print(occurrences[0])

url = 'https://d28rh4a8wq0iu5.cloudfront.net/ads1/data/ERR037900_1.first1000.fastq'      
first1000 = wget.download(url)

seqs, quals = readFastq(first1000)
seq_len = [len(i) for i in quals]
max(seq_len)

def phred33ToQ(qual):
    return ord(qual) - 33

phred33ToQ('#')
           
scores = [0]*100
for qual in quals:
    for i in range(100):
        scores[i] += phred33ToQ(qual[i])
avg_scores = [score/1000 for score in scores]


def createHist(qualities):
    hist = [0]*50
    for qual in qualities:
        for phred in qual:
            q = phred33ToQ(phred)
            hist[q] += 1
    return hist
h = createHist(quals)

len(h)
            

def qualBybase(qualities):
    scores = [0] *100
    for qual in qualities:
        for i in range(100):
            scores[i] += phred33ToQ(qual[i])
    avg_scores = [score/1000 for score in scores]
    return avg_scores

qualBybase(quals)
import matplotlib.pyplot as plt
plt.bar(range(60,70), avg_scores[60:70])

which(avg_score)        
    