
# Invert Hash

# A hash table / hash map is an obj / dictionary
# Given an object / dictionary,
# return a new object / dictionary that has the keys and the values swapped 
# so that the keys become the values and the values become the keys

# Input: { "name": "Zaphod", "charm": "high", "morals": "dicey" }
# Output: { "Zaphod": "name", "high": "charm", "dicey": "morals" }

""" thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
print(thisdict["brand"]) """


dict = { "name": "Zaphod", "charm": "high", "morals": "dicey" }

def findInvertDict(old_dict):
    new_dict = {}    
    for key in  old_dict:
        new_dict[old_dict[key]] = key #specific to Python
    return new_dict
print(findInvertDict(dict))


