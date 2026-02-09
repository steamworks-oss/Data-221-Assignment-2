from collections import Counter

with open("sample-file.txt", "r") as file:
    # read file by lines
    fileLines = list()
    normalizedLines = list()
    for line in file.readlines():
        # store original lines in a list
        fileLines.append(line)

        # convert line to lowercase
        line = line.lower()
        # remove all whitespaces and punctuation from line
        line = "".join(char for char in line if char.isalpha())
        # store updated lines into list
        normalizedLines.append(line)

# create counter object out of the normalized lines to see if they appear more than once
lineCounter = Counter(normalizedLines)
# get near-duplicate lines using the counter
lineDuplicates = [line for line, count in lineCounter.items() if line.isalpha() and count > 1]

# print out the number of lines that are identical after being normalized
print(f"There are {len(lineDuplicates)} duplicate line(s).\n")

# print out the first found near-duplicate line, with its line numbers, and the original lines
print(f"Near-Duplicate line: {lineDuplicates[0]}")
print(f"Line numbers: {[i+1 for i, line in enumerate(normalizedLines) if line == lineDuplicates[0]]}")
print(f"Original lines: {[fileLines[i] for i, line in enumerate(normalizedLines) if line == lineDuplicates[0]]}\n")

# print out the second near-duplicate line, with its line numbers, and the original lines
print(f"Near-Duplicate line: {lineDuplicates[1]}")
print(f"Line numbers: {[i+1 for i, line in enumerate(normalizedLines) if line == lineDuplicates[1]]}")
print(f"Original lines: {[fileLines[i] for i, line in enumerate(normalizedLines) if line == lineDuplicates[1]]}\n")

