import os
import random as rd

script = {
	0: ['Stinky.', 'Dum-dum.', 'Bruh.', '[insert insult here]', 'R U srs?', 'Weak.', 'Coward.', 'Coward!'],
	1: ['Lucky.', 'Did you cheat?', 'That\'s like one in a million!'],
	2: ['Lucky.', 'Wow!', 'U must be good at this... Unless you cheated...', 'That\'s rare.'],
	3: ['ez.', 'That was easy.', 'Good job!', '3 is da magic numba'],
	4: ['easy.', 'That was kinda easy.', 'Good job!', 'and flew gun flynn pour messes. BOOM IM DACTA SOOS'],
	5: ['ggs', 'That was fun.', 'Good job!', 'Play uggen pls.'],
	6: ['ggs?', 'That was pretty fun.', 'Good job!', 'I\'m 6 of this.'],
	7: ['took u a bit, dinnit?', 'That didn\'t seem to be easy.', 'Good job!', 'finally.'],
}

here = os.path.abspath(os.path.dirname(__file__))

def cls():
	os.system('cls')

def d2s(str1, str2): #difference of 2 strs
	ct = 0
	for t in range(3):
		ct += 1 if str1[t] != str2[t] else 0
	return ct

words = []
with open(f'{here}\\words\\3l.txt', 'r') as f:
	o = f.read().split('\n')
	for a in o:
		words.append(a.strip())

start = rd.choice(words)
end = rd.choice(words)
while start == end:
	end = rd.choice(words)

print("""
  Welcome to Word Chain!
   Change one three-letter word into another
 by changing one letter at a time. 
   Enter 'quit' to quit

      Example:

        dog
          |
        dot
        |
        cot
         |
        cat

   Enter to Start
""")
tidbit = ''
input()
cls()

g = 0
past = [start]
while True:
	g += 1
	print('', tidbit, f'\n {start} → {end}\n')

	for p in enumerate(past):
		print(f' [{p[0]}]   {p[1]}')
	if a == end:
		g -= 1
		ret = rd.choice(script[g]) if g < len(script.keys()) else 'You got there eventually.'
		print(f'You won in {g} guesses. {ret}')
		break

	a = input(f'[{g}]  >')
	cls()

	tidbit = ''
	if a == '':
		g -= 1
		continue

	if a == 'quit':
		print(f'You quit. {rd.choice(script[0])}')
		break

	elif a in words:
		if d2s(a, past[-1]) == 1:
			past.append(a)
		else:
			tidbit = '(!) only able to change one letter at a time'
			g -= 1
	else:
		tidbit = '(!) not a valid 3-letter word'
		g -= 1
input()