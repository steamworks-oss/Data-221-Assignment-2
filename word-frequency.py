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
# create counter object out of the tokens to get a collection of the words with their frequency
tokenFrequency = Counter(tokens)

# print out the ten most frequently occurring words along with their word count in descending order
for word, count in tokenFrequency.most_common(10):
    print(f"{word} -> {count}")
