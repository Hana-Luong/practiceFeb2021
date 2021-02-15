# Given an LIST of strings
# return a sum to represent how many times each list item is found (a frequency table)

# Input: ["a", "a", "a"]
# Output: {
#   "a": 3,
# }

# input =  ["a", "b", "a", "c", "B", "c", "c", "d"]
# Output: {
#   "a": 2,
#   "b": 1,
#   "c": 3,
#   "B": 1,
#   "d": 1,
# }

# https://www.w3schools.com/python/python_dictionaries_access.asp
# Get the value of the "model" key:
""" thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
x = thisdict["model"] """

#https://www.w3schools.com/python/gloss_python_access_list_items.asp
#How to access a list in Python
""" thislist = ["apple", "banana", "cherry"]
print(thislist[1]) """

# "in" and "not in" are keywords in Python

def findFrequency(aList):
    dict = {}
    for char in aList:
        if char not in dict:
            dict[char] = 1
        else: 
            dict[char] += 1
    return dict

print(findFrequency(["a", "b", "a", "c", "B", "c", "c", "d"]))


# Other solutions found by students from google
d = {}
for item in a:
    if item in d:
        d[item] = d.get(item)+1
    else:
        d[item] = 1

for k,v in d.items():
    print(str(k)+':'+str(v))
    
# below
def combine(input_string):
    import collections
    ctr = collections.Counter(input_string)
    return ctr
      
print(combine(["a", "a", "a","b", "c", "c", "d", "f", "f"]))
 
