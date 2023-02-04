# exercise-01 Vowel or Consonant

# Write the code that:
# 1. Prompts the user to enter a letter in the alphabet:
#      Please enter a letter from the alphabet (a-z or A-Z):
# 2. Write the code that determines whether the letter entered is a vowel
# 3. Print one of following messages (substituting the letter for x):
#      - The letter x is a vowel
#      - The letter x is a consonant
# Hints:  Use the in operator to check if a character is in another string
#         For example, if some_char in 'abc':

############## CODE START HERE #################

# alphabet = input('Please enter a letter from the alphabet (a-z or A-Z): ' ).lower()
# print(f'The user entered {alphabet}: ' )

# if alphabet in 'a e i o u':
#     print(f'The letter {alphabet} is a vowel')
# else:
#     print(f'The letter {alphabet} is a constant')

############# CODE END HERE ####################

# exercise-02 Length of Phrase

# Write the code that:
# 1. Prompts the user to enter a phrase:
#      Please enter a word or phrase:
# 2. Print the following message:
#      - What you entered is xx characters long
# 3. Return to step 1, unless the word 'quit' was entered.

############## CODE START HERE #################

# phrase = input('Please enter a word or phrase: ')
# print(f'What you entered is {phrase} characters long:',len(phrase))

############# CODE END HERE ####################

# exercise-03 Calculate Dog Years

# Write the code that:
# 1. Prompts the user to enter a dog's age in human years like this:
#      Input a dog's age in human years:
# 2. Calculates the equivalent dog years, where:
#      - The first two years count as 10 years each
#      - Any remaining years count as 7 years each
# 3. Prints the answer in the following format:
#      The dog's age in dog years is xx
# Hint:  Use the int() function to convert the string returned from input() into an integer

############## CODE START HERE #################

# dog_age = int(input('Input a dog\'s age in human years: '))
# dog_years = 0

# if dog_age <= 2:
#     dog_years = dog_age * 10
# else:
#     dog_years = 20 + (dog_age - 2) * 7

# print(f'The dog\'s age in dog years is {dog_years}')

############# CODE END HERE ####################

# exercise-04 What kind of Triangle?

# Write the code that:
# 1. Prompts the user to enter the three lengths of a triangle (one at a time):
#      Enter the lengths of three side of a triangle:
#      a:
#      b:
#      c:
# 2. Write the code that determines if the triangle is:
#      equalateral - all three sides are equal in length
#      scalene - all three sides are unequal in length
#      isosceles - two sides are the same length
# 3. Print a message such as:
#      - A triangle with sides of <a>, <b> & <c> is a <type of triangle> triangle

############## CODE START HERE #################

# a= int(input('Enter the lengths of side of a triangle a: '))
# b= int(input('Enter the lengths of side of a triangle b: '))
# c= int(input('Enter the lengths of side of a triangle c: '))
# if a == b == c:
#     print(f'A triangle with sides of {a}, {b} & {c} is a equalateral triangle')
# elif a != b != c:
#     print(f'A triangle with sides of {a}, {b} & {c} is a scalene triangle')
# else:
#     print(f'A triangle with sides of {a}, {b} & {c} is a isosceles triangle')


############# CODE END HERE ####################

# exercise-05 Fibonacci sequence for first 50 terms

# Write the code that:
# 1. Calculates and prints the first 50 terms of the fibonacci sequence.
# 2. Print each term and number as follows:
#      term: 0 / number: 0
#      term: 1 / number: 1
#      term: 2 / number: 1
#      term: 3 / number: 2
#      term: 4 / number: 3
#      term: 5 / number: 5
#      etc.
# Hint: The next number is found by adding the two numbers before it

############## CODE START HERE #################

# n1 = 0
# n2 = 1
# count = 0

# print(f'term: {count} / number: {n1}')
# print(f'term: {count+1} / number: {n2}')
# count += 2

# while count < 50:
#     n3 = n1 + n2
#     print(f'term: {count} / number: {n3}')
#     n1 = n2
#     n2 = n3
#     count += 1

############# CODE END HERE ####################

# exercise-06 What's the  Season?

# Write the code that:
# 1. Prompts the user to enter the month (as three characters):
#      Enter the month of the season (Jan - Dec):
# 2. Then promptshtt the user to enter the day of the month:
#      Enter the day of the month:
# 3. Calculate what season it is based upon this chart:
#      Dec 21 - Mar 19: Winter
#      Mar 20 - Jun 20: Spring
#      Jun 21 - Sep 21: Summer
#      Sep 22 - Dec 20: Fall
# 4. Print the result as follows:
#      <Mmm> <dd> is in <season>

# Hints:
# Consider using the in operator to check if a string is in a particular list/tuple like this:
# if input_month in ('Jan', 'Feb', 'Mar'):
# After setting the likely season, you can use another if...elif...else statement to "adjust" if
# the day number falls within a certain range.

############## CODE START HERE #################


############# CODE END HERE ####################