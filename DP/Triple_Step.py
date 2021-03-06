# problem 8.1 from page 145
"""
A child is running up a staircase with n steps and can hop either 1 step, 2 steps, or 3
steps at a time. Implement a method to count how many possible ways the child can run up the
stairs.
"""
import copy
def tripleStepRecursive(n, hops, hashmap = {}):
    if n in hashmap:
        return hashmap[n]

    if n == 0:
        return 1

    if n < 0:
        return None
    
    sum = 0
    for hop in hops:
        req_hop = n - hop
        
        returned = tripleStepRecursive(req_hop, hops)
        if returned != None:
            sum += returned
    
    hashmap[n] = sum
    return sum
    

def tripleStepTabular(n, hops):
    table = [0] * (n+1)
    curr = copy.deepcopy(table.pop(0))
    curr = 1
    table.insert(0, curr)
    

    for i in range(n+1):
        if table[i] > 0:
            for hop in hops:
                if i+hop <= n:
                    table[i+hop] += table[i]
    print(table)
    return table[n]

hops = [2,1]
# hops = [1,2,3]
# print(tripleStepRecursive(37, hops))
print(tripleStepTabular(5, hops))

# 11111
# 1112
# 1121
# 1211
# 2111
# 122
# 212
# 221





