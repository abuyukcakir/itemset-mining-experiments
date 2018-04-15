#!/usr/bin/env python3
import subprocess
def frequent_itemsets(filename, min_support, type='C'):
    p1 = subprocess.Popen(["./lcm", type, filename, str(min_support), "-"], stdout=subprocess.PIPE)
    
    itemsets = list(map(lambda x: (x.decode('utf-8')), p1.stdout.read().split(b'\n')))
    
    itemsets = list(map(lambda x: list(map(int, x.split())), itemsets))
    itemsets = itemsets[1:-1]
    return itemsets

