# write by number int dari 0 - 391
# for test apps form this project 
from random import seed
from random import randint
seed(1)
for _ in range(391):
	value = randint(0,391)
	print(value)