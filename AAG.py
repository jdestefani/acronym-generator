import itertools
import sys

if sys.version_info[0] < 3:
            raise Exception("Python 3 or a more recent version is required.")

longVersion = input("Insert the complete title of the article:")
tokens = longVersion.split(sep=" ")
uniqueLetters = [list(set(token)) for token in tokens]

print("[INFO] - Loading dictionary")
with open("wordsEn.txt") as word_file:
        dictionary = set(word.strip().lower() for word in word_file)

print("[INFO] - Generating acronyms")        
for element in itertools.product(*uniqueLetters):
    acronym = "".join(element).lower()
    if(acronym in dictionary):
        print("Found acronym: " + acronym)
    
