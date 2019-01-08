
text = "This is my test text. We 're keeping this text short to keep things manageable."

def count_words(text):
    '''
    Count the number of times each word occur in the text
    '''
    # change all words to lower case
    text = text.lower()
    # skip semicolon, colon, double quotes...
    skips = [".",",",";",":","'", '"']
    for ch in skips:
        text = text.replace(ch, "")

    # create an empty dictionary for words
    word_counts = {}
    # iterate each word through the list
    for word in text.split(" "):
        # known word
        if word in word_counts:
            word_counts[word] += 1
        else:
            word_counts[word] = 1
    return word_counts

print(count_words(text))

# Use function Counter from Module collections
from collections import Counter
def count_words_fast(text):
    '''
    Count the number of times each word occur in the text
    '''
    text = text.lower()
    skips = [".",",",";",":","'", '"']
    for ch in skips:
        text = text.replace(ch, "")

    word_counts = Counter(text.split(" "))
    return word_counts

print(count_words_fast(text))

#check if 2 function give the same result? Identical object
a= count_words(text) == count_words_fast(text)
print(a)

print(count_words("This comprehension check is to check for comprehension."))
b = len(count_words("This comprehension check is to check for comprehension."))
print(b)

# false because this 2 different objects
print(count_words(text) is count_words_fast(text))

# Reading a book from a file

def read_book(title_path):
    '''
    Read a book and return it as a string
    '''
    with open(title_path,"r", encoding= "utf8") as current_file:
        text = current_file.read()
        text = text.replace("\n", "").replace("\r","")
    return text


text = read_book ("/Users/tp10/Sanger_work/Developer101/python_for_research_edXcourse/Week_3/Books_EngFr/English/shakespeare/Romeo and Juliet.txt")
print(len(text)) # see how many characters

#Find location of a sentence (index)
ind = text.find("What's in a name?")
print(ind)

#Get the text from that location
sample_text = text[ind: ind + 1000]
print(sample_text)

def word_stats(word_counts):
    """return number of unique words and word frequencies"""
    num_unique = len(word_counts)
    counts = word_counts.values()
    return (num_unique, counts)

word_counts = count_words(text)
(num_unique, counts) = word_stats(word_counts)

print(num_unique, sum(counts))

text = read_book("/Users/tp10/Sanger_work/Developer101/python_for_research_edXcourse/Week_3/Books_GerPort/German/shakespeare/Romeo und Julia.txt")
word_counts = count_words(text)
(num_unique, counts) = word_stats(word_counts)
print(num_unique, sum(counts))
# contain 7527 words, in length 20311 


'''
Reading multiple files
'''
# use os module to read directories
import os
book_dir =("/Users/tp10/Sanger_work/Developer101/python_for_research_edXcourse/Week_3/Books")

# need to delete .DS_Store hidden file in the Book directory, otherwise it will throw an error
# open Termial, type this find /path/to-folder \( -name '.DS_Store' \) -delete
# find /Users/tp10/Sanger_work/Developer101/python_for_research_edXcourse/Week_3/Books \( -name '.DS_Store' \) -delete

print(os.listdir(book_dir))

import pandas as pd 
stats = pd.DataFrame(columns = ("language", "author", "title", "length", "unique"))
title_num = 1 

for language in os.listdir(book_dir):
    for author in os.listdir(book_dir + "/" + language):
        for title in os.listdir(book_dir + "/" + language + "/" + author):
            inputfile = book_dir + "/" + language + "/" + author + "/" + title
            print(inputfile)
            text = read_book(inputfile)
            (num_unique, counts) = word_stats(count_words(text))
            # store data
            stats.loc[title_num] = language, author.capitalize(), title.replace(".txt",""), sum(counts), num_unique
            title_num += 1

print (stats)
print(stats.head())
print(stats.tail())




'''
Intro to Pandas (panel data)
a library that provides additional data structure and data analysis functionalities.
useful for manipulating numerical tables and time series data
'''
import pandas as pd 
table = pd.DataFrame(columns = ("name","age"))
# row 1 of table
table.loc[1] = "James", 22
table.loc[2] = "Jess", 32
print(table)
print(table.columns)


'''
Use matplotlib.pyplot to plot the book length and unique word statistics 
'''
import matplotlib.pyplot as plt
plt.plot(stats.length, stats.unique,"bo")
plt.loglog(stats.length, stats.unique,"bo")

stats[stats.language == "English"]

stats[stats.language == "French"]

plt.figure(figsize =(10,10))
subset = stats[stats.language=="English"]
plt.loglog(subset.length, subset.unique,"o", label ="English", color="crimson")
subset = stats[stats.language=="French"]
plt.loglog(subset.length, subset.unique,"o", label ="French", color="forestgreen")
subset = stats[stats.language=="German"]
plt.loglog(subset.length, subset.unique,"o", label ="German", color="orange")
subset = stats[stats.language=="Portuguese"]
plt.loglog(subset.length, subset.unique,"o", label ="Portuguese", color="blueviolet")
plt.legend()
plt.xlabel("Book length")
plt.ylabel("Number of unique words")

plt.savefig("lang_plot.pdf")