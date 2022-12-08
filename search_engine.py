'''
Youre working on a search engine. Watch your back Google!

The given code takes a text and a word as input and passes them to a function called search().

The search() function should return "Word found" if the word is present in the text, or "Word not found", if its not.

Sample Input
"This is awesome"
"awesome"
Sample Output: Word found
'''
text = input()
word = input()

def search(word, text):
    if text in word:
        print('Word found')
    else:
        print('Word not found')

search(text, word)