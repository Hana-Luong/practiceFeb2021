# Zip Arrays into Map

# Given two arrays, create an associative array (aka hash map, an obj / dictionary) 
# containing keys from the first array, and values from the second.
# Associative arrays are sometimes called maps because a key (string) maps to a value 

# Input: ["abc", 3, "yo"], [42, "wassup", True]
# Output: {
#     "abc": 42,
#     3: "wassup",
#     "yo": True,
# }

# REMEMBER THIS
# https://www.w3schools.com/python/python_dictionaries_access.asp
# Get the value of the "model" key:
""" thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
x = thisdict["model"] """

keys = ["abc", 3, "yo"]
values = [42, "wassup", True]

def combined(keyKey,valueValue):
    newDict = {}
    for i in range(len(keyKey)):
        newDict[keyKey[i]] = valueValue[i]
    return newDict

print(combined(keys, values))
