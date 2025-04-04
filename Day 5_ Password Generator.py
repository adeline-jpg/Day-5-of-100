import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters = int(input("How many letters would you like in your password?\n"))
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))


#how I did it:
random_letters = random.sample(letters,nr_letters) #to take a random sample from your variable at the amount specified in input.
random_signals = random.sample(symbols, nr_symbols)
random_numbers = random.sample(numbers, nr_numbers)

for item in random_signals:
    random_letters.append(item)
item5 = random_letters
for item2 in random_numbers:
    item5.append(item2)
# print(*item5, sep="")
random.shuffle(item5)
print(*item5, sep="") #to remove the spaces and quotation marks/brackets

#solution for the easy version
password = "" #the reason why it came back with no brackets/quotation marks is because of "" for a string.
for char in range(0, nr_letters):
    password += random.choice(letters)

for char in range(0, nr_symbols):
    password += random.choice(symbols)

for char in range(0, nr_numbers):
    password += random.choice(numbers)

print(password)

#what the solution was (hard version):
password_list = [] #used [] to use list function append.
for char in range(0, nr_letters): #range from 0 to number specified with the input
    password_list.append(random.choice(letters)) #add onto password_list which is just []
for numb in range (0, nr_numbers):
    password_list.append(random.choice(numbers)) #the password_list from the last for function.
for symb in range (0, nr_symbols):
    password_list.append(random.choice(symbols))
random.shuffle(password_list) #shuffle the results.

password = "" #to change it into a string
for char in password_list:
    password += char

print(f"Your password is: {password}")
