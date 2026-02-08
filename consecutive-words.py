from string import punctuation
from collections import Counter

with open("sample-file.txt", "r") as file:
    # read file and split into words
    tokens = file.read().split()

# convert all words into lowercase
tokens = [token.lower() for token in tokens]
# remove punctuation from beginning and end of word
tokens = [token.strip(punctuation) for token in tokens]
# keep only words that contain at least two letters
tokens = list(filter(lambda token: len(token) >= 2, tokens))
# create bigram as tuples by zipping the word list without the last element with the word list without the first element
bigrams = list(zip(tokens[:-1], tokens[1:]))
# create counter object out of the bigrams to get a collection of the tuples with their frequency
bigramFrequency = Counter(bigrams)

# print out the five most frequently occurring bigrams along with their count in descending order
for bigram, count in bigramFrequency.most_common(5):
    print(f"{bigram[0]} {bigram[1]} -> {count}")