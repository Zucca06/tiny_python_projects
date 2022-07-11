#!/usr/bin/env python3
"""
Author : Michele Minervini
Date   : 11/07/2022
Purpose: Gashlycrumb
"""

dic = {}
file_name = 'gashlycrumb.txt'

letter = ' '

while(not letter == '!'):
  letter = input('Please provide a letter [! to quit]:')
  
  if letter.isalpha() and len(letter) == 1:
    with open(file_name) as file:
      for line in file:
        if letter.upper() == line[0].upper():
          dic[letter.upper()] = line
  else:
    error_string = f'I do not know "{letter}".\n'
    dic[letter.upper()] = error_string
  print(dic[letter.upper()], end = '')