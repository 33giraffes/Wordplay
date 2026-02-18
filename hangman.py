import os
from wonderwords import *

def cls():
	os.system('cls')

h = []
m = [' ',' ',' ',' ',' ',' ',' ']

w = RandomWord()
wrd = w.word(word_min_length=3, word_max_length=8)
wrd = wrd.lower()

PLAY = True
tidbit = ''
while PLAY:

	man = {
0: """
  [¯7¯|   
  ]/
  [
  ]
__[______
""",
1: f"""
  [¯7¯|
  ]/  O   {m[0]}
  [
  ]
__[______
""",
2: f"""
  [¯7¯|
  ]/  O   {m[0]} {m[1]}
  [   |
  ]
__[______
""",
3: f"""
  [¯7¯|
  ]/  O   {m[0]} {m[1]}
  [  /|   {m[2]}
  ]
__[______
""",
4: f"""
  [¯7¯|
  ]/  O   {m[0]} {m[1]}
  [  /|\\  {m[2]} {m[3]}
  ]
__[______
""",
5: f"""
  [¯7¯|
  ]/  O   {m[0]} {m[1]}
  [  /|\\  {m[2]} {m[3]}
  ]  /    {m[4]}
__[______
""",
6: f"""
  [¯7¯|
  ]/  O   {m[0]} {m[1]}
  [  /|\\  {m[2]} {m[3]}
  ]  / \\  {m[4]} {m[5]}
__[______
"""
	}

	cls()

	print(tidbit)
	print(man[m.index(' ')])

	guess = '-'*len(wrd)
	guess = list(guess)
	for l in enumerate(wrd):
		if l[1] in h:
			guess[l[0]] = l[1]
	guess = ''.join(guess)

	print(guess)

	if guess == wrd:
		print(f'\nYou Won! \nThe word was "{wrd}"')
		PLAY = False
		break

	elif m.index(' ') == 6:
		print(f'\nYou lost.\nThe word was "{wrd}"')
		PLAY = False
		break

	a = input('\nGuess a letter:\n> ')

	a = a.lower()
	if a.isalpha() and len(a) == 1 and a not in m and a not in h:
		if a in wrd:
			tidbit = f'(.) {a} was in the word'
			h.append(a)
		else:
			tidbit = f'(.) {a} was not in the word'
			m[m.index(' ')] = a
	else:
		if not a.isalpha() or len(a) != 1:
			tidbit = '(!) Not a letter'

		if a in m or a in h:
			tidbit = '(!) Already guessed'

input()

#==================================================================================================================