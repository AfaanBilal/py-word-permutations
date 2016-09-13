#
#    Py Word Permutations
#    
#    Author: Afaan Bilal
#    URL: https://afaan.ml
#    
#    Display all possible permutaions for a set of characters.
#    
#    (c) 2016 Afaan Bilal
#    Released under the MIT License
#
 
def base_convert(number, fromBase, toBase):
    i = 0
    result = 0
    number = int(number)
    while number > 0:
        result += (number % toBase) * (fromBase ** i)
        i += 1
        number //= toBase
    return str(result)
    
def binSearch(arr, s, ubound):
    b = 0
    t = ubound
    mid = (t + b) // 2
    
    if len(arr) <= mid:
        return False
    
    while b <= t:
        mid = (t + b) // 2
        if len(arr) <= mid:
            return False
        if arr[mid] < s:
            b = mid + 1
        elif arr[mid] > s:
            t = mid - 1
        else:
            return True
    else:
        return False
    
print("Py Word Permutations")
chars = input("Enter characters: ")

lcount = len(chars)
keys = ''.zfill(lcount)
chars = sorted(chars)

uchars = []

for c in chars[:]:
    if c in uchars:
        continue
    uchars.append(c)
    
ucount = len(uchars)
wcount = lcount ** lcount
real_wcount = ucount ** lcount

print("Total  Characters  : {}".format(lcount))
print("Total  Permutations: {}".format(wcount))
print("Unique Permutations: {}".format(real_wcount))

words = []
for i in range(wcount):
    cur_word = []
    for j in range(lcount):
        key = int(keys[j])
        cur_word.append(str(chars[int(key)]))
    
    c_word = ''.join(cur_word)
    keys = base_convert(keys, lcount, 10)
    keys_i = int(keys)
    keys_i += 1 
    keys = str(keys_i)
    keys = base_convert(keys, 10, lcount)
    keys = keys.zfill(lcount)
    
    if not binSearch(words, c_word, len(words)):
        words.append(c_word)
    
print("WORDS:")
for w in words:
    print(w, end=' ')
    
