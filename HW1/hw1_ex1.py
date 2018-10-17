#Ex1a
import string
alphabet = string.ascii_letters

#Ex1b
sentence = 'Jim quickly realized that the beautiful gowns are expensive'

count_letters = {}
#write your code here!
count = 0
for letter in sentence:
    if letter in alphabet:
        keys = count_letters.keys()
        if letter in keys:
            if letter.isupper():
                count_letters[letter]+=1
            else:
                count_letters[letter]+=1
        else:
            if letter.isupper():
                count_letters[letter]=1
            else: 
                count_letters[letter]=1

print (count_letters)

#Ex1c
# Create your function here!

def counter(input_string):
    count_letters = {}
    for letter in sentence:
        if letter in alphabet:
            keys = count_letters.keys()
            if letter in keys:
                if letter.isupper():
                    count_letters[letter]+=1
                else:
                    count_letters[letter]+=1
            else:
                if letter.isupper():
                    count_letters[letter]=1
                else: 
                    count_letters[letter]=1
    return count_letters

counter(sentence)

#Ex1d
address_count = counter(address)
print(address_count)

#Ex1e
# write your code here!
max = 0
for keys in address_count:
    if address_count[keys] > max:
        max = address_count[keys]
    else:
        max = max

for keys, values in address_count.items():
    if values == max:
        most_frequent_letter = keys
        

print(most_frequent_letter)