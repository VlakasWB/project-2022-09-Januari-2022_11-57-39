# write by number int dari 0 - 85
# for test apps form this project 
from random import seed
from random import randint
seed(1)
for _ in range(85):
	value = randint(0,85)
	print(value)