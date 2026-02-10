# Data 221 - Assignment 2

<u>word-frequency.py:</u>
- Reads from a text file and splits it into a list of words.
- It then takes the lowercase of each word, strips each word of punctuation at the beginning and end, and filters out words less than two alphabetic characters.
- Prints out the ten most frequent words from the above list along with their tally occurrences in descending order.

<u>consecutive-words.py:</u>
- Reads from a text file and splits it into a list of words.
- It then takes the lowercase of each word, strips each word of punctuation at the beginning and end, and filters out words less than two alphabetic characters.
- Create bigrams from the processed word list, and then counts the frequency of each bigram.
- Prints out the five most frequent bigrams along with their tally occurrences in descending order.

<u>near-duplicate-lines.py:</u>
- Read lines from a text file and convert them into lowercase, and remove all whitespace and punctuation.
- Identifies the processed lines that are duplicates and then prints the number of duplicates.
- Prints the first two found duplicate lines, along with their original line numbers and original form.

<u>filter-tabular-data.py:</u>
- Loads a dataset of students into a DataFrame.
- Filter DataFrame by study time, internet usage, and absences of students and save as a new dataset.
- Print the number of students in the updated DataFrame along with their average grade.

<u>generate-grouped-summary-table.py:</u>
- Loads a dataset of students into a DataFrame.
- Creates a new column calculated by the grades of the students. Then generates a grouped summary table from the new column with the number of students, average absences, and percentage of students with internet access
- Save the summary table to a CSV file.


<u>compare-categories.py</u>
- Loads a dataset of crime statistics into a DataFrame.
- Creates a new "risk" column based on the violent crimes per population column. Then groups the data by the new column and calculates the average unemployment rate for each group.
- Prints the average unemployment rate for both risk groups.

<u>scrape-webpage-paragraph.py</u>
- Scrapes the wikipedia entry for Data science.
- Extracts and prints the title of the article.
- Extracts and prints the first paragraph of the main text with at least 50 characters.

<u>scrape-webpage-header.py</u>
- Scrapes the wikipedia entry for Data science.
- Extracts the \<h2> section headers but filters out the headings containing certain words. ("References, "External links", "See also", "Notes")
- Removes "[edit]" substring from remaining headers and then saves them to a text file line by line.

<u>scrape-tabular-data.py</u>
- Scrapes the wikipedia entry for Machine learns.
- Converts first table with at least three data rows into a DataFrame. Fills in headers and values if empty.
- Saves extracted table to a CSV file.