# -*- coding: utf-8 -*-
"""
Created on Thu Jun  6 16:48:46 2019

@author: Himanshu Rathore
"""

file_name = input("Please enter file name:")

def word_count(file_name):
    
    with open(file_name, mode='rt') as file:
        
        list_of_lines = file.readlines()
        lines_count = len(list_of_lines)
        
        word_dict = {}
        characters_count = 0
        
        for line in list_of_lines:
            words_list = line.split()
            characters_count += len(line)
        
            for word in words_list:
                
                if word not in list(word_dict.keys()):
                    word_dict[ word ] = 1
                else:
                    word_dict[ word ] += 1
            
        unique_words_count = len(list(word_dict.keys()))
        
        words_count = 0
        for value in word_dict.values():
            words_count += value
        
    return characters_count, words_count, lines_count, unique_words_count

characters, words, lines, uniq_words = word_count(file_name)
print("Total Characters:",characters)
print("Total words:",words)
print("Total Lines:",lines)
print("Total Unique Words:",uniq_words)       