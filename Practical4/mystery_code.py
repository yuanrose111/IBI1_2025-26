# What does this piece of code do?
# Answer: This code import the randint function from the random library and ceil function from the math library (though ceil is unused),
# then uses a while loop to generate 11 random integers between 1 and 10, sums these integers, and prints the total sum.

# Import the randint function from the random library to generate random integers within a specified range
# Example: randint(1,5) returns a random integer between 1 and 5 (inclusive)
from random import randint  

# Import the ceil function from the math library (this function is not used in the code)
# The ceil function rounds a number up to the nearest integer 
from math import ceil  

# Initialize a variable to store the cumulative sum of random numbers, starting at 0
total_rand = 0  

# Initialize a progress counter to control the number of loop iterations, starting at 0
progress = 0    

# Start a while loop that runs as long as the progress counter is less than or equal to 10
# This loop will execute 11 times (progress values: 0 → 1 → ... → 10)
while progress <= 10:  
    progress += 1       # Increment the progress counter by 1 for each loop iteration
    n = randint(1, 10)  # Generate a random integer between 1 and 10 (inclusive) and assign to variable 'n'
    total_rand += n     # Add the newly generated random number 'n' to the cumulative sum

# Print the final total sum of all 11 random integers
print(total_rand)  