import string
from typing import List
class Solution:
    def uniqueMorseRepresentations(self, words: List[str]) -> int:
        morse = [".-","-...","-.-.","-..",".","..-.","--.","....",
        "..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.",
        "...","-","..-","...-",".--","-..-","-.--","--.."]
        alpha = list(string.ascii_lowercase)
        d = {}
        for i in range(len(morse)):
            d[alpha[i]] = morse[i]
        trans = set()
        for word in words:
            builder = []
            for char in word:
                builder.append(d[char])
            trans.add(''.join(builder))
        return len(trans)
    
    def commentedVersion(self, words: List[str]) -> int:
        # use the mapped version of morse code provided
        morse = [".-","-...","-.-.","-..",".","..-.","--.","....",
        "..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.",
        "...","-","..-","...-",".--","-..-","-.--","--.."]
        # creating a list of lowercase chars a-z
        alpha = list(string.ascii_lowercase)
        # dictionary to hold char: morse pairs
        d = {}
        # loop over both lists to create the pairs
        for i in range(len(morse)):
            d[alpha[i]] = morse[i]
        # create a set to hold the unique concats
        trans = set()
        # loop over each word
        for word in words:
            # create a new list to hold all the concats for this word
            builder = []
            # loop over each char
            for char in word:
                # find the morse code for each letter and append onto builder
                builder.append(d[char])
            # join the list into final morse code for word and add to set
            trans.add(''.join(builder))
        # len of set will give us all unique morse
        return len(trans)