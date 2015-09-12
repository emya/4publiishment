from random import randint
import sys
from copy import deepcopy
import math

argvs = sys.argv

#${leng} ${leng} ${an} ${input} ${out}

num_steps = 200

#leng = 50

lenp = 1036
lens = 155

sum_mat = [[0 for i in range(lenp)] for j in range(lens)]
#mat[len_p][len_s]

def check_mat(mat, b_mat):#check whether new mat == before mat 
    return mat == b_mat

def decident(mat):
    match = False 

    while match is False:
        i = randint(0, lenp-1)
        j = randint(0, lens-1)
        if mat[i][j] == 1:
           match = True 

    return i, j

def m_c(bmat, original_s, original_p, ith, jth, p):
    mat = deepcopy(bmat)
    marginal_p = [sum(mat[i]) for i in range(lenp)]
    marginal_s = [0 for i in range(lens)]
    for i in range(lens):
        s = 0
        for j in range(lenp):
            s += mat[j][i]
        marginal_s[i] = s

    if marginal_p == original_p and marginal_s == original_s:
        i, j = decident(mat)
        mat[i][j] = 0
        p = 0
        return mat, i, j, p
        #return mat, ith, jth, p
    else:
        """
        if mat[ith][jth] == 0:
            mat[ith][jth] = 1
            p = 1
            return mat, ith, jth, p
        else:
        """
        match = False
        while match is False:
            k = randint(0, lenp-1)
            l = randint(0, lens-1)
            if mat[k][l] == 1 or (k == ith and l == jth):
                match = True

        if k == ith and l == jth:
            mat[ith][jth] = 1
            p = 1
            return mat, ith, jth, p
        else:
            if randint(0, 9) < 5:
                if mat[k][jth] == 0:
                    mat[k][jth] = 1
                    mat[k][l] = 0
                    jth = l
                    p = 0
                return mat, ith, jth, p
                #return mat, k, h, p

            else:
                if mat[ith][l] == 0:
                    mat[ith][l] = 1
                    mat[k][l] = 0
                    ith = k
                    p = 0
                return mat, ith, jth, p

def jaccade(mat):
    jmat = [[0 for i in range(lenp)] for j in range(lenp)]
    for i in range(lenp):
        for j in range(i+1, lenp):
            c = 0
            for k in range(lens): 
                if mat[i][k]+mat[j][k] == 1: 
                    c += 1 
            jmat[i][j] = c
            jmat[j][i] = c
    return jmat


def mcmc(num, d_file, o_file):
    original_data = []
    f = open(d_file, "r")
    for line in f:
        l = line.replace('\n', '').split(' ')
        #print "l", l
        original_data.append([int(x) for x in l])
    f.close()

    original_p = [sum(original_data[i]) for i in range(lenp)]
    original_s = [0 for i in range(lens)]
    for i in range(lens):
        s = 0
        for j in range(lenp):
            s += original_data[j][i]
        original_s[i] = s

    original_jmat = jaccade(original_data)
    count_n = 0

    bmat = original_data

    cmat = [[0 for i in range(lenp)] for j in range(lenp)]
    
    p = 1
    mi = -1
    mj = -1

    while count_n < num:
        mat, mi, mj, p = m_c(bmat, original_s, original_p, mi, mj, p)
        jmat = jaccade(mat)

        for i in range(lenp):
            for j in range(i+1, lenp):
                if jmat[i][j] >= original_jmat[i][j]:
                    cmat[i][j] += 1
                    cmat[j][i] += 1
        count_n += 1
        bmat = deepcopy(mat)

    tru = []
    fal = []

    f = open(o_file+str(num)+".txt", 'w')
    pmat = [[0 for i in range(lenp)] for j in range(lenp)]
    for i in range(lenp):
        ll = []
        for j in range(lenp):
            if i == j:
                c = 1.0
            elif cmat[i][j] == 0:
                c = 0.5/num
                #c = -math.log10(cc)
            else: 
                c = cmat[i][j]/float(num)
                #c = -math.log10(cc)
            ll.append(c)
        f.write(' '.join([str(x) for x in ll])+'\n')
         
    f.close()

mcmc(num_steps, "data_4.txt", "data_4_pmat")
