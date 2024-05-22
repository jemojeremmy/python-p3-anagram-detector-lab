# your code goes here!
# lib/anagram.py

class Anagram:
    def __init__(self, word):
        self.word = word
    
    def match(self, word_list):
        matches = []
        sorted_word = sorted(self.word)
        for candidate in word_list:
            if sorted(candidate) == sorted_word:
                matches.append(candidate)
        return matches
