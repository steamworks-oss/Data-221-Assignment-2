def find_lines_containing(filename, keyword):
    # read through each line of file; if keyword is in line, add it to a list with the line number and line text
    with open(filename, "r") as file:
        matchingLines = list()
        count = 0
        for line in file.readlines():
            count += 1
            if keyword in line:
                matchingLines.append((count, line))
    return matchingLines

# test the function
filename = "sample-file.txt"
keyword = "lorem"
matchingLines = find_lines_containing(filename, keyword)

# print the number of matching lines and the first 3 matching lines
print(f"There are {len(matchingLines)} lines containing {keyword} in {filename}")
print(f"The first three matching lines are:")
for lineNumber, lineText in matchingLines[:3]:
    print(f"{lineNumber}, {lineText}:")

