#!/usr/bin/env python

genefile = 'data_4_name.txt'
p_file = 'data_4_together_pmat200.txt'

b_pvalue = 0.01

f = open(p_file, 'r')

p = []

for line in f:
    l = line.replace('\n','').split(' ')
    p.append([float(x) for x in l])
f.close()

fg = open(genefile, 'r')
gl = fg.readline()
fg.close()

g_list = gl.split(' ')

fo = open("data_4_together_pairs_genes.txt", "w")
for i in range(len(p)):
    for j in range(i+1, len(p[i])):
        if p[i][j] <= b_pvalue and p[i][j] != 0:
             fo.write(g_list[i]+" : "+g_list[j]+" ; "+str(p[i][j])+"\n")
fo.close()
             
       
