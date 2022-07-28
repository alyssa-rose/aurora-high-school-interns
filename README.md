# Aaron and Alyssa's Machine Learning Crash Course

## Introduction
Hey y'all! This is a repository (basically a place to keep code and track changes to that code). Feel free to poke around on Gitlab to get familiar. An alternative is also Github, which you might've heard of. They are both places to house code. 

This repository is meant to give a small introduction to Python, coding best practices, and machine learning. For the first section, I have included a Python file (a .py file) which you can run and play with. For the other sections, it is up to you to learn how to create a new Python file, and then code in it. If you have any questions, be sure to message the group chat. However, I encourage you to:
1. Try to solve the problem on your own first by experimentation and Googling
2. Work with each other if you're still stuck
3. Reach out to the group chat that has Aaron and Alyssa in it if you want some extra help!

    

# Course

## Intro to Python
### Downloading an IDE (integrated development environment)

Spyder is an easy to use IDE, which can be downloaded here: https://www.spyder-ide.org/#section-download

This will come with Python built in already, so you don't have to worry about downloading Python separately.





### Pseudo Code

The file can be found here: https://gitlab-ee.aurora.aero/Rose.Alyssa/high-school-interns/-/blob/main/pseudo_code_example.py

This is meant to give you an introduction to what pseudocoding is, and how to write comments in Python. Additionally, there is a small bit of Python code, which you should get familiar with and try to understand what's going on and how to do it yourself! Feel free to play around with the variables to see how stuff changes.

To run the code, you can download the repository by selecting the download icon:

![download_icon](/pictures_for_readme/downloading_repository.PNG)



You can then open Spyder and open the file within Spyder:

![spyder_open_file](/pictures_for_readme/open_file_spyder.PNG)



And then run the file:

![spyder_run_file](/pictures_for_readme/run_file_spyder.PNG)



You will see the output of the file here:

![spyder_output](/pictures_for_readme/file_output_spyder.PNG)


To make a new file:

![make_new_file](/pictures_for_readme/make_new_file.PNG)


and then save that file:

![save_new_file](/pictures_for_readme/save_new_file.PNG)



### An Intro Course to Python

Now that you know how to create Python files and run them, let's put it to action! Here are two intro courses for you to complete that provide an amazing introduction to Python: 
1. https://www.kaggle.com/learn/intro-to-programming
2. https://www.kaggle.com/learn/python

If you want to go further into some of the topics, I have provided the below subsections with more information:

#### Python Types

It's important to have a solid understanding of the foundation of Python. Specifically, some of the types (variables that you can declare) are 
important to know. A (non comprehensive) list of them can be found here: https://docs.python.org/3/tutorial/introduction.html

The above document details numbers, strings, and lists, which are core Python types. Feel free to create a new Python file in Spyder, and 
declare your own variables (whether it's a number (`some_number = 5`), a string (`some_string = "Aurora"`), or a list (`some_list = []` or 
`some_list = list()`))




#### Python Control Flow

Once you are able to make some variables, it is worthwhile to *do* something with those variables. This is where Python control flows come 
into play. You can read about them here: https://docs.python.org/3/tutorial/controlflow.html
 
Again, I encourage you to get creative! Make a problem you want to solve (like printing letters in a word, or only printing numbers if they're 
divisible by five), and then implement it! This will help you develop coding and problem solving skills.



#### Python Data Structures

Now that we have variables and ways of manipulating them, we want to be able to store them and manipulate further. In the pseudo_code_example.
py file, you saw that we used strings and lists, and manipulated them in some way. In this document: https://docs.python.org/3/tutorial/
datastructures.html , you can learn more about all the cool things that lists and other data structures do. Really take your time to read, 
research, and ask questions with this!


#### Installing Python packages

This is not important for right now, but will be later. 

A Python package is code that was written in Python, and packaged neatly such that it can be used over and over again. Here is a great explanation of a Python package: https://www.udacity.com/blog/2021/01/what-is-a-python-package.html

Some of these packages are already built into the core Python library, and some have to be installed. In order to install a Python package, you will use `pip` on the command line. 

Using pip is specified here: https://www.datacamp.com/tutorial/python-install-pip

For example though, if you want to install `numpy`, you would run `pip install numpy` on the command line. Once installed, you can open Spyder, and run `import numpy`.




## Machine Learning Intro:

For this section, will be using this course: https://www.kaggle.com/learn/intro-to-machine-learning

I have also provided some subsections below to help!


#### Terminology

Here is a glossary that you can search in if you come across a Machine Learning term that you are unsure of: https://developers.google.com/
machine-learning/glossary


#### Machine Learning Workflow

Here is a general workflow that can be followed when doing machine learning: https://cloud.google.com/ai-platform/docs/ml-solutions-overview

#### Pandas

Pandas (`import pandas as pd` as you will usually see it), is a powerful Python package that is used as the main data structure package in ML. Here is a course on it: https://www.kaggle.com/learn/pandas


## Intermediate Machine Learning

Now that you have a great idea of the workflows and processes of one machine learning model, it is time to expand to others:
https://developers.google.com/machine-learning/crash-course

This course is MUCH more in depth, and will take longer than you will probably be at Aurora. However, I encourage you to do everything to the best of your ability, and come to Aaron and Alyssa with questions in the group chat. I also encourage you to talk to each other and share knowledge. This course is very high level, and contains some math that you will encounter in college. Because of this, do not feel scared or intimidated by it!


## AI Ethics

Most importantly, it is crucial to understand how the things you build impact the world. Our machine learning models are also human to the extent that we build them, and we build our biases and prejudices into them. Here is a course on AI ethics: https://www.kaggle.com/learn/intro-to-ai-ethics


## Final Project

Hope you've had so much fun! I know that this is overwhelming, but you have learned so much. In this final section, I encourage you to find some data that excites you (https://www.kaggle.com/datasets), and do something cool with it! In this part you should:

1. Determine if you want to do supervised (https://developers.google.com/machine-learning/glossary#supervised-machine-learning) or unsupervised (https://developers.google.com/machine-learning/glossary#unsupervised-machine-learning) learning
2. Find a dataset that matches the scope (if you're doing supervised, the dataset should have `ground truth` labels. I.e. the thing you're trying to predict. Having ground truth labels will tell you how close you were to the actual answer).
3. Pick a handful of models that you want to try. Think about why you would pick some over others.
4. Preprocess your data
5. Write the models
6. Train the models
7. Test the models! See which one did the best on the test set.

## Extra challenge mode

If you really want to deep dive into learning how to read a machine learning paper, I first recommend starting with this: https://www.researchgate.net/profile/Batta-Mahesh/publication/344717762_Machine_Learning_Algorithms_-A_Review/links/5f8b2365299bf1b53e2d243a/Machine-Learning-Algorithms-A-Review.pdf?eid=5082902844932096 which talks about different machine learning models!

