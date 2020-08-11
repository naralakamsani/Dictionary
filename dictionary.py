# import
import json
from difflib import get_close_matches

# load the data
data = json.load(open("data.json"))

# function to get defintion of a given word
def translate(w):
    
    # Get rid of any errors in case of user input
    w = w.lower()
    
    # find def if the word is correctly spelled by user
    if w in data:
        return data[w]
    
    # Check words that are similar in spelling if no word asked by use exists
    elif len(get_close_matches(w, data.keys())) > 0:
        yn = input("Did you mean %s instead? Enter Y if yes, or N if no: " % get_close_matches(w, data.keys())[0])
        if yn == "Y":
            return data[get_close_matches(w, data.keys())[0]]
        elif yn == "N":
            return "The word doesn't exist. Please double check it."
        else:
            return "We didn't understand your entry."\
        
    # If no similar word exists
    else:
        return "The word doesn't exist. Please double check it."

# Take user input
word = input("Enter word: ")

# Find the output
output = translate(word)

# If the word has mulitple definitions
if type(output) == list:
    for item in output:
        print(item)
        
#If the word only has one definition
else:
    print(output)
