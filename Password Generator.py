import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters= int(input("How many letters would you like in your password?\n")) 
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

#Eazy Level - Order not randomised:
#example- JduE&!91
password=""

for char in range(1, nr_letters + 1):
        password += random.choice(letters)
   
for char in range(1, nr_numbers +1):
        password+= random.choice(numbers)

for char in range(1, nr_symbols +1):
        password += random.choice(symbols)

print(f"The Simple Password is {password}")   
print("As seen the password character order is not randomized\n")         

#Hard Level - Order of characters randomised:
#example- g^2jk8&P


password_list= []

for char in range(1, nr_letters + 1):
        password_list.append(random.choice(letters))
   
for char in range(1, nr_numbers +1):
        password_list.append(random.choice(numbers))

for char in range(1, nr_symbols +1):
        password_list.append(random.choice(symbols))

#print(password_list)    

new_password=""
random.shuffle(password_list)
for char in password_list:
       new_password += char


print(f"The new difficult password is {new_password}")    
print("As seen the password character order is randomized!")



