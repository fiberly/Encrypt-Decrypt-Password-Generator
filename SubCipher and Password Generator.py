import random
import string
import os
import re

#Subs Cipher Part
class SubstitutionCipher:
    def __init__(self):
        self.alphabet = string.ascii_lowercase
        self.key = ''.join(random.sample(self.alphabet, len(self.alphabet)))

  # define encryption and decryption
    def encrypt(self, plaintext):
        # Encrypt plaintext using the substitution cipher key
        plaintext = plaintext.lower()
        return ''.join(self.alphabet[self.key.index(char)] if char in self.alphabet else char for char in plaintext)

  
    def decrypt(self, ciphertext):
        # Decrypt ciphertext back to plaintext using the substitution cipher key
        return ''.join(self.alphabet[self.key.index(char)] if char in self.key else char for char in ciphertext)

#User input Cipher and display
def handle_encrypt_decrypt(cipher):
        print("\nEncrypt/Decrypt Data: ")
        print("1. User Input")
        print("2. File Content")
        choice = input("Enter your choice (1/2): ")

        if choice == '1':
            data  = input("Enter the text to encrypt: ")
        elif choice == '2':
            filename = input("Enter the filename: ")
            if not os.path.isfile(filename):
                print(f"File '{filename} not found.")
                return
            with open(filename, 'r') as file:
                data = file.read()
        else:
            print("Invalid Choice")
            return
        
    #Output
        print("\nOriginal Plaintext:")
        print(data)

        encrypted = cipher.encrypt(data)
        print("\nEncrypted Text:")
        print(encrypted)

        decrypted = cipher.decrypt(encrypted)
        print("\nDecrypted Text:")
        print(decrypted)



# Password Generator Part
def checkPasswordComplexity(password):

    # Make a counter variable and set to 0
    complexityCounter=0 
    # Check if the password is at least 8 characters long
    if len(password) < 8:
        return False

    # Check if the password contains at least one uppercase letter
    if not re.search(r'[A-Z]', password):
        complexityCounter+=1

    # Check if the password contains at least one lowercase letter
    if not re.search(r'[a-z]', password):
        complexityCounter+=1

    # Check if the password contains at least one digit
    if not re.search(r'\d', password):
        complexityCounter+=1
    
    # Check if the password contains at least one symbol
    if not re.search(r'[\W_]', password): 
        complexityCounter+=1

    # If more than 1 instance of the password not being complex enough is found, returns false. Else, returns true
    if complexityCounter>1:
        return False
    else:
        return True


# Defines a generatePassword function, with length, uppercase, lowercase, numeric and symbol parameters
def generatedPassword(length, uppercase, lowercase, numeric, symbol): 
     
     # Creates an empty string with if statements, that add the uppercase, lowercase, numbers or punctuation symbols to the original string
    chars = ""
    if uppercase:
        chars += string.ascii_uppercase
    if lowercase:
        chars += string.ascii_lowercase
    if numeric:
        chars += string.digits
    if symbol:
        chars += string.punctuation

# If all zeros are selected, this ensures proper error handling
    if len(chars) == 0:
        return ''

        

# Creates a new password string variable, along with a for loop, 
# taking the range of the length of the input, appending a random choice of characters from 
# the appended chars variable, to the newPassword variable 
    newPassword = ''
    for test in range(length):
        newPassword += random.choice(chars)

    return newPassword



def passwordGenerator():

    attemptsMaximum = 7
    attemptCount = 0

    # Outer restart loop
    while True: 
        
        print('\n|        Password Generator          |\n|Enter a positive integer from 1-500 |\n|(EXIT = 0)                          |')
        print('|Passwords need at least 8 characters|\n|  and at least 3 of the following:  |\n| 1 symbol, 1 number, 1 uppercase    |\n|    and one lowercase character     |\n')
        
        # initializing variables with a default value
        uppercaseResponse = 0
        lowercaseResponse = 0
        numericResponse = 0
        symbolResponse = 0

        # While loop to iterate through the lengthResponse and corresponding code
        while True: 
            # Error handling for a number greater than 500, and a number less than or equal to zero
            try: 
                # ask user what they want
                # Takes user input asking for length of characters of password
               # securePasswordRequirementGeneration = int(input('Would you like the password generator to run without the requirements?'))
                lengthResponse = int(input("How long do you want your password to be? "))
                
                # checks for zero entry, closing the program if 0 is entered
                if lengthResponse == 0:
                    print("\nExiting password generator...\n")
                    return
                # checks for a password of less than 8 characters
                if lengthResponse < 8:
                    print('Password must be at least 8 characters')
                    continue
                
                
                
                
                # while loop, checks if the condition in if statement is true and if is continues to the next line(s), if not, re-runs the loop
                # Checks if the input password length is less than or equal to 500 characters
                if lengthResponse <= 500:
                    print('\n \n')
                else: 
                    
                    print('\n! Maximum character limit must be less than or equal to 500 !\n')
                    print('-----------------------------------------------------------------\n')
                    
                    continue
                
                # while loop, checks if the condition in if statement is true and if is continues to the next line(s), if not, re-runs the loop
                # Checks if length response is zero and not negative
                if lengthResponse < 0:
                    print("\n ! Please enter a positive number that is not zero !\n")
                    print('-----------------------------------------------------------------\n')
                    continue        
                break
            # Checks if the entry for complexity, is a one or zero
            except ValueError:
                print('\n! Please enter a number !\n')
                print('-----------------------------------------------------------------\n')
            
      
        # While loop to loop through user input, if the value is not correct according to the code, loop repeats.
        while True: 
            # Try and except for checking user input being a zero or one 
            try: 
                # Takes user input for uppercase, lowercase, numeric and symbols, user can enter a 1 for yes and 0 for no
                uppercaseResponse = int(input("\nDo you want to include UPPERCASE characters? (1 = YES, 0 = NO, 3 = EXIT, 4 = RESET) \n"))
                if uppercaseResponse == 3:
                    print("\nExiting password generator...\n")
                    return
                elif uppercaseResponse == 4:
                    print("\nResetting the password generation process...\n")
                    break
                elif uppercaseResponse not in [0, 1, 3, 4, int('01')]:
                    print('Please enter the numbers that are listed, 0, 1, 3, or 4')
                    continue

                lowercaseResponse = int(input("Do you want to include lowercase characters? (1 = YES, 0 = NO, 3 = EXIT, 4 = RESET) \n"))
                if lowercaseResponse == 3:
                    print("\nExiting password generator...\n")
                    return
                if lowercaseResponse == 4:
                    print("\nResetting the password generation process...\n")
                    break
                if lowercaseResponse not in [0, 1, 3, 4]:
                    print('Please enter the numbers that are listed, 0, 1, 3, or 4')
                    continue

                numericResponse = int(input("Do you want to include numeric 0-9 characters? (1 = YES, 0 = NO, 3 = EXIT, 4 = RESET) \n"))
                if numericResponse == 3:
                    print("\nExiting password generator...\n")
                    return
                if numericResponse == 4:
                    print("\nResetting the password generation process...\n")
                    break
                if numericResponse not in [0, 1, 3, 4]:
                    print('Please enter the numbers that are listed, 0, 1, 3, or 4')
                    continue
                
                symbolResponse = int(input("Do you want to include symbol characters? (1 = YES, 0 = NO, 3 = EXIT, 4 = RESET) \n"))
                if symbolResponse == 3:
                    print("\nExiting password generator...\n")
                    return
                if symbolResponse == 4:
                    print("\nResetting password generator...\n")
                    break
                if symbolResponse not in [0, 1, 3, 4]:
                    print('Please enter the numbers that are listed, 0, 1, 3, or 4')
                    continue
                break

            except ValueError:
                print('\n!Please enter a number being either 0, 1, 3, 4 !\n')
                print('-----------------------------------------------------------------\n')
            

            # prints the generatePassword function, with the input values of zero or one, matching up with the original function in location, 
            # calling the if statements, then looping through the appended chars string, with a random choice of characters from 
            # ascii_uppercase, ascii_lowercase, digits and punctuation, printing the randomized collage of the previously mentioned characters. 
        print('\n')
        
       
        # print(f'{checkPasswordComplexity(password)}')
        while True:
            password = generatedPassword(lengthResponse, uppercaseResponse, lowercaseResponse, numericResponse, symbolResponse)
            if password == '':
                print('\n! At least one character type must be selected. !\n') 
            else: 
                print(f'Here is your password, though may not meet requirements, which are at least 3 of the following, \n[1 symbol, 1 number, 1 uppercase and one lowercase character] : \n\n -> {password}')        
            print('\n')
            if checkPasswordComplexity(password) == True: 
                print(f'Generated Password, that meets requirements, is: \n -> {password}')
                break
            else: 
                attemptCount += 1
                print('\nGenerated password has not met the criteria, which are at least 3 of the following, \n[1 symbol, 1 number, 1 uppercase and one lowercase character], regenerating now...\n\n')
                

            if attemptCount >= attemptsMaximum:
                print(f'\nExceeded maximum password generation, exiting password generation now. Would you like to reset or exit?\n')
                reQu = int(input('enter 3 = QUIT or 4 = RESET: '))
                if reQu == 3:
                    print('\n Shutting down password generator...\n')
                    return
                elif reQu == 4:
                    print('\nRestarting password generator...\n')
                    break
                else: 
                    print('Choice needs to be a 3 or 4')
                    return
            break
            
        if any([uppercaseResponse == 4, lowercaseResponse == 4, numericResponse == 4, symbolResponse == 4]):
                continue
        
        if any([uppercaseResponse == 3, lowercaseResponse == 3, numericResponse == 3, symbolResponse == 3]):
                break


        # Asks user to if they want to generate another password, if the response is not yes, the loop breaks and the program ends
        while True: 
            try: 
                restart = int(input("\nDo you want to generate another password? (1 = YES, 0 = NO): ").strip().lower())
                if restart == 1:
                    print("\nRestarting password generator...\n")
                    break
                elif restart == 0:
                    print("\n Shutting down password generator...\n")
                    return
                else: 
                    print('Please enter a [yes or no]')
                break
            except ValueError:
                print('Please enter a number being 1 for yes or 0 for no')
 
        

#Main Menu and functionality
def main_menu():

    # Display the main menu and handle user choices
    cipher = SubstitutionCipher()

    while True:
        print("\nMain Menu:")
        print("1. Encrypt/Decrypt Data (User Input or File)")
        print("2. Generate a Password")
        print("3. Exit")
        choice = input("Enter your choice 1, 2, or 3: ")

        if choice == '1': 
            handle_encrypt_decrypt(cipher)
        if choice == '2':
            passwordGenerator()
        elif choice =='3':
            print("Have a good time!")
            break
        else:
            print("\nPlease pick only 1, 2, or 3")

    




#Run the program Dont touch
if __name__ == "__main__":
    main_menu()
