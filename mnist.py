#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Apr 15 15:44:32 2018

@author: serkan
"""
import numpy as np
import pandas as pd
from matplotlib import pyplot as plt
import seaborn as sns
from scipy.io import loadmat
import subprocess
from sklearn.preprocessing import StandardScaler
from sklearn.datasets.mldata import fetch_mldata

def frequent_itemsets(filename, min_support, type='C'):
    def split_itemset(str):
        itemsets = str.split()
        if (len(itemsets) < 2):
            return None
        
        freq = itemsets[-1]
        freq = freq[1:-1]
    
        return int(freq), list(map(int, itemsets[0:-1]))
    
    p1 = subprocess.Popen(["./lcm", '{}f'.format(type), filename, str(min_support), "-"], stdout=subprocess.PIPE)
    
    output = p1.communicate(str.encode("utf-8"))[0]
    output = output.decode('utf-8')
    itemsets = output.split('\n')
    
    itemsets = list(map(split_itemset, itemsets))
    itemsets = list(filter(None.__ne__, itemsets))
    return itemsets

mnist_path = "mnist"
digits = fetch_mldata('mnist-original', data_home=mnist_path)

features = digits.data
labels   = digits.target

class_0 = features[labels == 0 , :]

transactions = []
for i in range(class_0.shape[0]):
    transactions.append(np.where(class_0[i, :] > 50)[0].tolist())
    

with open('s.txt','w') as fp:
    for i in range(class_0.shape[0]):
        fp.write(' '.join(map(str, transactions[i])))
        if (i + 1 != class_0.shape[0]):
            fp.write('\n')


itemsets = frequent_itemsets("s.txt", 4000, type='M')

mm = 0
mi = 0
a = np.zeros((28 * 28))
for freq, itemset in itemsets:
    if (len(itemset) > mm):
        mm = len(itemset)
        mi = itemset
    for item in itemset:
        a[item] = 1
        
plt.figure()
plt.imshow(a.reshape(28, 28), cmap='gray')
plt.show()
