# write by number int dari 0 - 277
# for test apps form this project 
from random import seed
from random import randint
seed(1)
for _ in range(277):
	value = randint(0,277)
	print(value)