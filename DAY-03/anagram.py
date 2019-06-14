# -*- coding: utf-8 -*-
"""
Created on Wed Jun  5 17:36:26 2019

@author: Himanshu Rathore
"""

word1 = input("Enter 1st word: ")
word2 = input("Enter 2nd word: ")

def anagram_check(word1,word2):
    
    characters_in_word1 = set(word1)
    characters_in_word2 = set(word2)
    
    if characters_in_word1 == characters_in_word2 and len(word1) == len(word2):
        return True
    else:
        return False
    
print("Anagram:",anagram_check(word1,word2))