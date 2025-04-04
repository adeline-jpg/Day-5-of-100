# Day-5-of-100
## Password Generator

Today I've learned about loops. I'm going to deviate from my usualy template for READMes because, well, I don't know much about these loops. 

I have seen loops in action but actually writing the bit? Idk its very hard. This concept requires a new level of creativity, in my opinion. I got the concept down, looping through a list, etc. and so far I've only learned about for loops. 

I understand it easily enough, but when combined with other things that i have learned e.g. conditionals or even mathmatical operators, I get confused. 

So that means I don't understand it at all. 

I am writing and submitting this repository, but I'm going to take a break from learning new items for a few days. I'm going to grasp all the concepts I learned so far, and I'll be sure to return more proficient at the concepts that I was confused about.

here are some examples and definitions that I could look back on: 

## Loops 
- Loops allow us to tell the computer to repeat actions without having to write repeated code.
### Syntax: 
``` javascript
for <variable name of each item> in <a List>:
    <do something>
    <do something else>
```
### Examples: 
``` javascript
fruits = ["Apple", "Peach", "Pear"]
for fruit in fruits:
    print(fruit)
    print(fruit + " pie")
```
TIP: indentation really matters. Within an indentation and it is within the code, and out of the indentation, it is somethin separate.

## For Loops with Range 
- The combination of the range() function with the Python For Loop allows us to run a loop for as many times as we wish. Instead of looping through each item in a List, we can loop through a range of numbers.
- ***Not to be confused with the range calculation of max-min
### Syntax 
``` javascript
for number in range(1, 10): #this will print 1 to 9 
    print(number)
```
### Example
```javascript
sum1 = 0
for number in range (1,101):
    sum1 += number
```
## Example of loops and conditionals together 
- remember this symbol "%"? well, she's back.
``` javascript
for numbers in range (1,101):
    if numbers % 3 == 0 and numbers % 5 == 0:
        print("FizzBuzz")
    elif numbers % 3 == 0:
        print("Fizz")
    elif numbers % 5 == 0:
        print("Buzz")
    else: 
        print(numbers)
```


