# write by number int dari 0 - 611
# for test apps form this project 
from random import seed
from random import randint
seed(1)
for _ in range(611):
	value = randint(0,611)
	print(value)