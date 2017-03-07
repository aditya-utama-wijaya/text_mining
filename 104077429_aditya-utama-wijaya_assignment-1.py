
# coding: utf-8

# # Read sentences from file "building_global_community.txt"

# In[1]:

sentences = [line.strip() for line in open('2-building_global_community.txt')]
sentences


# # Split sentences into words

# In[2]:

from nltk import wordpunct_tokenize
list_of_words = [wordpunct_tokenize(sentence) for sentence in sentences]
list_of_words


# In[3]:

words = [word for list_of_word in list_of_words for word in list_of_word]
words


# # Filter out symbols (isalpha, isdigit, isalnum)

# In[4]:

words = [word for word in words if word.isalpha() == True or word.isdigit() == True or word.isalnum() == True]
words


# # Normalize words

# In[5]:

words = [word.lower() for word in words]
words


# # Filter out stopwords

# In[6]:

from nltk.corpus import stopwords
stopwords = set(stopwords.words('english'))
words = [word for word in words if word not in stopwords]
words


# # Count the occurrences of words

# In[7]:

from collections import Counter
counter = Counter(words)
counter.most_common()


# # Save result to CSV file

# In[8]:

import csv
with open('104077429_aditya-utama-wijaya_wordcount.csv', 'w') as csvfile:
    fieldnames = ['word', 'count']
    writer = csv.DictWriter(csvfile, fieldnames = fieldnames)
    writer.writeheader()
    for word, count in counter.most_common():
        writer.writerow({'word': word, 'count': count})


# # Read CSV

# In[9]:

with open('104077429_aditya-utama-wijaya_wordcount.csv') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        print(row['word'], row['count'])


# # Words with POS (part-of-speech)

# In[10]:

from nltk.tag import pos_tag, map_tag
tagged_words = pos_tag(words)
simplified_tagged_words = [(word, map_tag('en-ptb', 'universal', tag)) for word, tag in tagged_words]
simplified_tagged_words


# In[11]:

from collections import defaultdict
posWordCounter = defaultdict(Counter)
for word, pos in simplified_tagged_words:
    posWordCounter[pos][word] += 1


# In[12]:

for pos, counter in posWordCounter.items():
    print(pos, ': ', end = '')
    for word, count in counter.most_common(5):
        print(word, '|', count, end = ', ')
    print()

