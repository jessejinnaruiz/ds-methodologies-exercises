'''
Count how many key strokes it takes to 'text' a word on a phone dial pad.
'''
letters = [['a', 'b', 'c'],['d', 'e', 'f'],['g', 'h', 'i'],['j', 'k' , 'l'],['m', 'n', 'o'],['p', 'q', 'r', 's'],['t', 'u', 'v'],['w', 'x', 'y', 'z']]

keys = [i+2 for i in range(8)]
print(keys)

# dict_dialpad = {keys:letters}
# print(dict_dialpad)

# for i in len(letters):
#     print(letters[i])


print(len(letters))