
# Invert Hash

# A hash table / hash map is an obj / dictionary
# Given an object / dictionary,
# return a new object / dictionary that has the keys and the values swapped 
# so that the keys become the values and the values become the keys

# Input: { "name": "Zaphod", "charm": "high", "morals": "dicey" }
# Output: { "Zaphod": "name", "high": "charm", "dicey": "morals" }


def invert_hash(given_dict):
    new_dict = {}
    for keys in given_dict:
        new_dict[given_dict[keys]]= keys
    return new_dict
result = invert_hash({ "name": "Zaphod", "charm": "high", "morals": "dicey" })
print (result)

def invert_hash(object):
    new_dict = {}
    for k, v in object.items():
        if v in new_dict:
            new_dict[v].append(k)
        else:
            new_dict[v] = k
    return new_dict

result = invert_hash({ "name": "Zaphod", "charm": "high", "morals": "dicey" })
print(result)




