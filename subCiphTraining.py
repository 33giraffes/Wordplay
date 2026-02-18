#=Imports==========================================================================================================

import os
from wonderwords import *

#=definitions======================================================================================================

def cls():
	os.system('cls')

here = os.path.abspath(os.path.dirname(__file__))

def d2s(str1, str2): #difference of 2 strs
	if len(str1) > len(str2):
		str2 += '\n'*(len(str1) - len(str2))
	elif len(str1) < len(str2):
		str1 += '\n'*(len(str2) - len(str1))

	ct = 0
	for t in range(len(str1)):
		if str1[t] != str2[t]:
			ct += 1
	return ct

#=Codes/Ciphers====================================================================================================

codefiles = {}
for f in os.listdir(f'{here}\\codes'):
	path = f'{here}\\codes\\{f}'
	if os.path.isfile(path):
		codefiles[f[:-4]] = path

codes = {}
for cf in codefiles.keys():
	with open(codefiles[cf]) as C:
		ctext = C.read().split('\n')
		oto = {}
		for t in ctext:
			o = t.split('=')
			oto[o[0]] = o[1]
		codes[cf] = oto

#=Start============================================================================================================

print('Welcome to Substitution Cipher Training!\nplease select a cipher:')
x = 1
for code in codes.keys():
	print(f'[{x}]', code)
	x += 1
print()
q = 1234567889976

while int(q) >= x:
	q = input('> ')
	while not q.isnumeric():
		q = input('> ')

#=Game=============================================================================================================

#=Word=#

cls()
print('You chose', list(codes.keys())[int(q) - 1])
print('\nLet\'s start easy. \nTranslate this word:')
nw = RandomWord()
plain = nw.word()
ccph = list(codes.values())[int(q) - 1]

cipher = ''
for a in plain:
	cipher += ccph[a.upper()]
print('\n', cipher, '\n')

a = input()
str_diff = d2s(a.upper(), plain.upper())
if str_diff == 0:

	#=Sentence=#

	print(f'That\'s right! The word was {plain}')
	input()
	cls()

	print('Time to bump up the difficulty!\nTraslate this sentence:')

	rs = RandomSentence()
	plain = rs.sentence()

	cipher = ''
	for a in plain:
		cipher += ccph[a.upper()]

	print('\n', cipher, '\n')

	a = input()
	stc_diff = d2s(a.upper(), plain.upper())
	if stc_diff == 0:
		print('Congratulations! you finished your training.')

	elif stc_diff <= 3:
		print(f'So close! It was "{plain}"')

	else:
		print(f'Nope, it was "{plain}"')

elif str_diff == 1:
	print(f'So close! It was "{plain}"')
else:
	print(f'Nope, it was "{plain}"')

input()

#=End==============================================================================================================