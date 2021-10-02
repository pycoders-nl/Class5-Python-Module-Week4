# Class5-Python-Module-Week4

## 1. Password
Write a Python program to check the validity of a password (input from users)
    
**Rules :**
- At least 1 letter between [a-z] and 1 letter between [A-Z]
- At least 1 number between [0-9].
- At least 1 character from [$#@].
- Minimum length 6 characters.
- Maximum length 16 characters.

If password is not valid throw `ValueError` with a proper error message for each rule. If the password is valid print a success message. Use some from  `raise`, `except`, `assert`, `else` and `finally` keywords.

## 2. Dice Percentage
Create an array with 6 elements named `dice`. Fill this array with the value zero. Generate a random number with a value between 1 and 6 (just like a **dice**) in a repetition 5000 times.

If the value is 1, increase the element 0 in the array by 1, the same applies to the values 2, 3, 4, 5 and 6. The dice[0] element indicates the number of times value 1 has occurred. Or in general: dice[x-1] indicates the number of times that x has been thrown. 
    
At the end of the repetition, print the contents of the array as percentages with 2 decimal places. For example; `"Percentage of throws of value 3 = 16.28%"`

## 3. Basic Import
Create a Python module called `my_dice.py` and export the code you wrote in question 2 into a function called `rollDice(number)`. 

Changes:
- Instead of repetition of 5000 times, makes a repetition of times of given `number` variable.
- Instead of printing, return the array of percentages.

Then create a new module called `main.py`. Gets an input from the user using `"Enter repetition number: "`. Then call rollDice method with this user input. Lastly, print each probability. E.g. `"The probability of 0 is 16.20"`

## 4. The Greatest Common Divisor
As a user, I want to use a program which can calculate the `greatest common divisor (GCD)` of my inputs. 

Acceptance Criteria:
- Ask user the enter the number of inputs (n).
- Ask user to enter `n` input numbers one by one.
- Use try/except blocks to verify input entries and warn the user for Nan or non numerical inputs.
- Calculate the greatest common divisor (GCD) of `n` numbers.
- Use `gcd` function in module of math.

## Hackerrank Questions

1. Diagonal Difference: https://www.hackerrank.com/challenges/diagonal-difference/problem

2. Left Rotation: https://www.hackerrank.com/challenges/array-left-rotation/problem

3. Counter game: https://www.hackerrank.com/challenges/counter-game/problem

4. Time Delta: https://www.hackerrank.com/challenges/python-time-delta/problem
