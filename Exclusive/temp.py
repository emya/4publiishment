#!/usr/bin/env python

import transfer_concretedata as tc
import poiss_binomial as poi

def pos_neg(mat):
    pos = []
    neg = []
    for i in range(len(mat)):
        for j in range(i+1, len(mat)):
            if (i==0 and j==1) or (i==3 and j==4):
               pos.append(mat[i][j])
            else: neg.append(mat[i][j])
    print "pos", pos
    print "neg", neg

datafile = "datasimulationout-proposedmcmcp_exclusive_len50sig15vari1.5noise8.0.out"

m = []

f = open(datafile, 'r')

for line in f:
    list = line.replace('\n', '').split(' ')
    m.append([int(x) for x in list])

f.close()

poi_pmat_p, poi_pmat_s = poi.poisson_p(m)

print "pppppppppppppppppppppppppppppp"
pos_neg(poi_pmat_p)
print "ssssssssssssssssssssssssssssss"
pos_neg(poi_pmat_s)

