# What does this piece of code do?
# Answer: Generating random integers from 1 to 10 for 11 times, summing them up, and print the final result.

# Import libraries
# randint allows drawing a random number,
# e.g. randint(1,5) draws a number between 1 and 5
from random import randint

# ceil takes the ceiling of a number, i.e. the next higher integer.
# e.g. ceil(4.2)=5
from math import ceil
# Initialise total grand and porgress
total_rand = 0
progress=0
# Loop while progress is less than or equal to 10
while progress<=10:
    # Increase progress by 1 at the start of each loop
	progress+=1
	n = randint(1,10)
	# Add the random number n to the total sum
	total_rand+=n

print(total_rand)

