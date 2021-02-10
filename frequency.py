# Given an LIST of strings
# return a sum to represent how many times each list item is found (a frequency table)

# Input: ["a", "a", "a"]
# Output: {
#   "a": 3,
# }

# Input: ["a", "b", "a", "c", "B", "c", "c", "d"]
# Output: {
#   "a": 2,
#   "b": 1,
#   "c": 3,
#   "B": 1,
#   "d": 1,
# }



## This one works YAY!

def counter_list(listy):
    new_dict = {} 
    for letter in listy:
        if letter in new_dict: # for every letter in 
            new_dict[letter] += 1
        else:
            new_dict[letter] = 1

    return new_dict

print(counter_list(["a", "b", "a", "c", "B", "c", "c", "d"]))
print(counter_list(['a','b']))

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

