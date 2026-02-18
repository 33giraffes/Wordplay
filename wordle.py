#=Imports==========================================================================================================

import os
import random as rd

#=Definitions======================================================================================================

def cls():
	os.system('cls')

here = os.path.abspath(os.path.dirname(__file__))

symbs = {
	0: ' ',
	1: '#',
	2: ':',
	3: '|'
}

letters = 'qwertyuiopasdfghjklzxcvbnm'
hm = {}
for i in range(26):
	hm[letters[i]] = 0

words = []
with open(f'{here}\\words\\5l.txt', 'r') as f:
	o = f.read().split('\n')
	for a in o:
		words.append(a.strip())

wrd = rd.choice(words)
guess = ['-','-','-','-','-']
below = [' ',' ',' ',' ',' ',]
past = []
for i in range(6):
	past.append('-----')
	past.append('     ')

#=Main=Loop========================================================================================================

g = 0
tidbit = ''
PLAY = True
while PLAY:
	g += 1
	cls()
	print()
	
	#=Top=#

	if g == 1:
		print('       Welcome to Wordle!')
	print(f''' {tidbit}

 #&# =  not in word  = '
 :&: =    in word    = *
 |&| = in right spot = ^

 guessed {g - 1}/6

	''')

	#=Guesses=#

	past[past.index('-----')] = ''.join(guess)
	past[past.index('     ')] = ''.join(below)

	for p in past:
		print(' '*13 + p)
	below = [' ',' ',' ',' ',' ',]


	#=Key=Board=#

	kb = ' '
	for i in range(26):
		ltt = letters[i]

		kb += f'{symbs[hm[ltt]]}{ltt}{symbs[hm[ltt]]}'

		if ltt in 'pl':
			kb += '\n' + ' '*((-(ord(ltt)//4 - 28)*2)+2)
	print(kb)

	#=Win/Lose=#

	if wrd == ''.join(guess):
		print(f'\n You Win! The word was "{wrd}"')
		break

	elif g > 6:
		print(f'\n You Lose. The word was "{wrd}"')
		break

	#=Answer=#

	if g > 1 and ans in words:
		pass#t.append(ans)
	ans = input('\n Enter a 5-letter word:\n > ').lower()

	#=Validity=#

	guess = ['-','-','-','-','-']
	if ans == '':
		tidbit = ''
		g -= 1

	elif ans not in words:
		tidbit = '(!) not a valid 5-letter word'
		g -= 1
	else:

		tidbit = ''
		guess = list(ans)
		for a in enumerate(guess):
			nbool = wrd.count(a[1]) 

			if a[1] in wrd and ans[:a[0]].count(a[1]) < wrd.count(a[1]):
				below[a[0]] = '*'
				hm[a[1]] = 2 if hm[a[1]] != 3 else 3
			else:
				below[a[0]] = '\''
				hm[a[1]] = 1 if hm[a[1]] < 2 else hm[a[1]]

			if a[1] == wrd[a[0]]:
				below[a[0]] = '^'
				hm[a[1]] = 3
	
input()

#==================================================================================================================