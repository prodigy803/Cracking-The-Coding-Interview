# problem 8.1 from page 145

# def tripleStepRecursive(n, hops):
#     if n == 0:
#         return []

#     if n < 0:
#         return None

#     for hop in hops:
#         req_hop = n - hop
        
#         returned = tripleStepRecursive(req_hop, hops)
#         print('returned', returned)
#         if returned != None:
#             returned.append(hop)
#             return returned

#     return returned

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





