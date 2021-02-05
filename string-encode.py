# String Encode
# You are given a string that may contain sequences of consecutive characters.
# Create a function to shorten a string by including the character,
# then the number of times it appears. 


# str1 = "aaaabbcddd"
# expected1 = "a4b2c1d3"

def encode_string(stringy_string):
    result = ""
    counter = {}
    for char in stringy_string:
        if char not in counter:
            counter[char] = 1
        else:
            counter[char] += 1
    for key in counter:
        result += key
        result += str(counter[key])
    return result


encoded_string = encode_string("aaaabbcccdddddfffffffff")
print(encoded_string)