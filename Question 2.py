'''
Card to Value Tuple
Write a function card_to_value_tuple that takes in a playing card of as a string of format '{rank}{suit}' and returns a tuple of integers format (suit_value, rank_value) as described below.

The suit values from low to high:

S (Spades) - 1
H (Hearts) - 2
D (Diamonds) - 3
C (Clubs) - 4
The rank values from low to high:

A (Ace) - 1
2 through 10 - same as the number
J (Jack) - 11
Q (Queen) - 12
K (King) - 13
NOTE: This is a function type question, you don't have to take input or print the output, just have to complete the required function definition.

Example

>>> card_to_value_tuple('AH')
(2, 1)
>>> card_to_value_tuple('7D')
(3, 7)
>>> card_to_value_tuple('QS')
(1, 12)
>>> card_to_value_tuple('9C')
(4, 9)
>>> card_to_value_tuple('10D')
(3, 10)
'''
