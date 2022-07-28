# -*- coding: utf-8 -*-
"""
Created on Thu Jul 28 09:46:47 2022

@author: Alyssa Bekai Rose

The purpose of this Python file is to show you what pseudo code is, and why
Python is *basically* psuedocode. Sure it can get more involved as you learn,
but for the meantime, it's a very beginner friendly programming language.

Pseudocode in essence, are comments that help you plan out code before you
start writing the code. There is an old saying of "whiteboard before keyboard",
which basically means you should plan out ahead of time what you're going to code,
how you're going to structure it, and what you expect to happen.

Below I show you the 3 different ways to write Python comments:
"""

# 1.
# this is a Python comment

# 2.
""" 
This is also a Python comment, but is used generally if you have

a

lot

of

things

to

say
"""

# 3.
''' You can also use apostrophes instead of quotes to write the long comments!'''


""" *********************************************************************** """
""" ********************** PSEUDO CODE EXAMPLE **************************** """
""" *********************************************************************** """

# Pseudo code is again, just comments that can help you plan out what you
# want to code ahead of time. Learning to properly plan out code and
# comment your code well is a hallmark of a great programmer. 

# Let's say I want to loop over a word, and print out each letter, then
# add the letter to a list, and rejoin the letters back into the word. Here is the pseudocode:
    
    
    
'''
0.) create a word
1.) Make an empty list that we can add to
2.) for each letter in the word
       a.) print out each letter
       b.) add the letter to a list
       c.) print the list
3.) print the full list
4.) rejoin the letters (elements) of the list to make the original word
5.) print the original word
'''

# and here is the code with comments (always! comment! your! code!)


word_to_print = "aurora"  # we have initialized a string, which is anything contained in " " or ' '
list_to_add_to = []  # this is how you make a list. You can also do: list_to_add_to = list()

# iterate over each of the letters in the word, this is a for loop!
for letter in word_to_print:  
    print("Printing the letter: {}".format(letter))
    list_to_add_to.append(letter)
    print(list_to_add_to)
    
# we are now outside the for loop, which means the for loop is over now!

print("Full List: {}".format(list_to_add_to)) # the list with all the letters in it
rejoined_original_word = ''.join(list_to_add_to) # join all the letters back into a string
print("Original Word: {}".format(rejoined_original_word))





















