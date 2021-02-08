# String Decode  
# Given an encoded string in the following format: letter, number, etc...  
# decode the string into its original format

# Get the value of the "model" key:
""" thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
x = thisdict["model"] """
# the following: dictionary[encoded[idx]] 
# encoded[idx] = the key, meaning "a", "b", "c", "d"

# This can only work if the numbers are single digits

encoded = "a2b4c3d7"
output = "aabbbbcccddddddd"

def decode(any_string):
    print(any_string)
    dictionary = {}
    result = ""
    # Objective 1: Build a dictionary like this {'a': 2, 'b': 4, 'c': 3, 'd': '7'}    
    for idx in range(len(encoded)):
        # Objective 1a: find the keys of the dictionary. They are encoded[idx] if idx even
        # Objective 1b: Build the values of the dictionary
        if idx % 2 == 0:
            dictionary[encoded[idx]] = ""
            print(dictionary)
            
            # idx = 0 => {'a': ''} 
            # idx = 2 =>  {'a': 2, 'b': ''} 
            # idx = 4 =>  {'a': 2, 'b': 4, 'c': ''}
            # idx = 6 =>  {'a': 2, 'b': 4, 'c': 3, 'd': ''}

        else:
            # The int imposition is important
            dictionary[encoded[idx-1]] = int(encoded[idx])
            # idx = 1 => {'a': '2'}
            # idx = 3 => {'a': 2, 'b': 4} 
            # idx = 5 => {'a': 2, 'b': 4, 'c': 3} 
            # idx = 7 =>  {{'a': 2, 'b': 4, 'c': 3, 'd': '7'}
    
    # Objective 2: concatenate to get the result
    for key in dictionary:
        # this print command is not necessary. It shows key-value pairs so we can check.
        print(key, dictionary[key])
        #a 2
        #b 4
        #c 3
        #d 7
        result += key * dictionary[key]
    print(result)

decode(encoded)