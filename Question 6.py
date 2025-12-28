'''
Text Frequency Analysis
Write a function analyse_text(sentence, task) that analyzes a given sentence and computes results based on the task specified. It uses helper sub-functions to achieve the following tasks:

count_non_whitespace - Returns the total number of characters in the sentence, excluding spaces and newline characters.
most_frequent_char - Returns the most frequent character in the sentence(case insensitive) as a lowercase alphabet. In case of a tie, return the largest character in alphabetical order.
count_diverse_words - Returns the number of words that contain more than 5 distinct characters(case insensitive i.e, "A" and "a" is considered same.).
word_with_highest_char_frequency - Returns the word that has the highest frequency of any single character (case insensitive). In case of a tie, return the word that appears first.
NOTE: Assume words are separated by spaces, do not consider non alphabetic chars in the analysis

NOTE: This is a function-type question. You do not have to take input or print the output. Just complete the required function. You may define helper functions inside the main function if needed.

Examples

>>> sentence = """Python is fun, programming is awesome."""
>>> analyse_text(sentence, "count_non_whitespace")
33
>>> analyse_text(sentence, "most_frequent_char")
'i'
>>> analyse_text(sentence, "count_diverse_words")
3
>>> analyse_text(sentence, "word_with_highest_char_frequency")
'programming'
'''
