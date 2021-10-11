# with open('sample.txt','r') as f:
#     for lines in f:
#         print(f.read())

# f = open('sample.txt')
# flines = f.readlines()
# for line in flines:
#     print(line)

# f = open('sample.txt','r')
# print(f.readline(),end='')
# print(f.readline(),end='')
# print(f.readline(),end='')

# a = 'BHav,ya, Raj'
# print(a.split(','))

# f = open('car.png','rb')
# f2 = open('2.png','wb')
# for i in f:
#     f2.write(i)

# def Counting():
#     file_name = input('Enter the name of file: \t')
#     num_words = 0
#     num_letters = 0
#     with open(file_name,'r') as f:
#         for line in f:
#             words = len(line.split())
#             letters = len(line)
#             num_letters += letters
#             num_words += words
#         num_letters -= words
#     print(num_words)
#     print(num_letters)
# Counting()

import random
a = ['Rock', 'Paper', 'Scissor']
print(random.choice(a))