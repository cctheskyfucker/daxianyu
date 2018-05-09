dicta = {}
dictb = {}
store_c = []
dist_list = []
sample_total = 0
from collections import defaultdict
from vector import *
from functools import reduce
from random import sample
import time

def read_digit(fp):
    bits = fp.read(32*33).replace('\n','')
    if bits == '':
        return -1,-1
    vec = list(map(int,bits))
    label = int(fp.readline())
    return label, vec
# open files 
# return labels and vectors 
def global_data(file):
    global dicta
    dicta = defaultdict(list)
    with open(file) as fp:
        while True:
            l,v = read_digit(fp)
            if l == -1:
                break
            dicta[l].append(v)
def vec_distance(v):
    for i in dicta.keys():
        for j in dicta[i]:
            d = distance(j,v)
            dist_list.append((i,d))
def show_info_a():
    global sample_total
    l = sorted(dicta.keys())
    for i in l:
        vec = dicta[i]
        print('          {} = {}'.format(i,len(vec)))
        sample_total += len(vec)
def global_data_sec(file):
    global dictb
    dictb = defaultdict(list)
    with open(file) as fp:
        while True:
            l,v = read_digit(fp)
            if l == -1:
                break
            dictb[l].append(v)
def most_common(s_l):
    counter = []
    for i in s_l:
        counter.append(i[0])
    return max(set(counter), key=counter.count)
def test_main():
    global sample_total
    global_data('digit-training.txt')
    global_data_sec('digit-testing.txt')
    fin = []
    for i in dictb.values():
        for j in i:
            vec_distance(j)
            sorted_list = sorted(dist_list, key=lambda dist: dist[1])[0:9]
            common = most_common(sorted_list)
            fin.append(common)
            dist_list.clear()
    print('-------------------------------------------')
    print('               Training Info               ')
    print('-------------------------------------------')
    show_info_a()
    print('-------------------------------------------')
    print('           Total Samples =',sample_total,'              ')
    print('-------------------------------------------')
    sample_total = 0
    print()
    print('-------------------------------------------')
    print('               Testing Info               ')
    print('-------------------------------------------')
    save = []
    l = sorted(dictb.keys())
    for a in dictb.keys():
        leng = len(dictb[a])
        le = fin[0:leng].count(a)
        fin = fin[leng:]
        save.append((a,leng,le,leng-le))
    sorted_save = sorted(save, key=lambda dist: dist[0]) 
    w_guess = 0
    c_guess = 0
    for i in l:
        vec = dictb[i]
        per = sorted_save[i][2]/len(dictb[i])
        print('          {} = {} , {}, {}'.format(i,len(vec),sorted_save[i][3],str(int(per*100))+'%'))
        sample_total += len(vec)
        w_guess += per*100
        c_guess += sorted_save[i][2]
    print('-------------------------------------------')
    print('            Accuracy = ',round(w_guess/10,4),'%',sep = '')
    print('          Correct/Total = ',c_guess,'/',sample_total,sep = '')
    print('-------------------------------------------')
def global_data_third(file):
    global store_c
    with open(file) as fp:
        while True:
            l,v = read_digit(fp)
            if l == -1:
                break
            store_c.append(v)
def perdict():
    global_data_third('digit-predict.txt')
    perdict = []
    for i in store_c:
        vec_distance(i)
        sorted_list = sorted(dist_list, key=lambda dist: dist[1])[0:9]
        common = most_common(sorted_list)
        perdict.append(common)
        dist_list.clear()
    for i in perdict: 
        print(i)
def main():
    print('Beginning of Training @ ', time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()))
    test_main()
    print('End of Training @',time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()))
    perdict()

main()