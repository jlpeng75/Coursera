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
    fh = open(filename, "r")
    for line in fh:
        genome = ""
        if not line.startwith(">"):
            genome += line.rstrip()
        return genome

genome = readGenome('lambda_virus.fa')



fh = open(filename, 'r')
for line in fh: 
    genome = ''
    if not line.startwith(">"):
         genome += line.rstrip()
    return genome


        