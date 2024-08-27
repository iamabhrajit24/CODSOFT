# CODSOFT
IN THIS THERE IS SPECIFICATIONS OR CAN BE SAID SUMMARY OF THE TASKS COMPLETED FOR THE INTERNSHIP AND TASKS GIVEN
3 TASKS COMPLETED

TASK 2: Calculator Program 

Purpose:

This Python program is designed to perform various mathematical operations, providing a basic command-line interface for users to select and execute calculations.

Core Features:

Operations Supported:

Addition (+): Adds two numbers.
Subtraction (-): Subtracts the second number from the first.
Multiplication (*): Multiplies two numbers.
Division (/): Divides the first number by the second. Includes error handling for division by zero.
Exponentiation (^): Raises the first number to the power of the second number.
Square Root (√): Computes the square root of a non-negative number. Handles errors for negative inputs.
Sine (sin): Calculates the sine of an angle in degrees.
Cosine (cos): Calculates the cosine of an angle in degrees.
Tangent (tan): Calculates the tangent of an angle in degrees.
Logarithm (log): Computes the natural logarithm (base e) of a positive number. Includes error handling for non-positive inputs.

User Interface:

The program begins by displaying a menu with the list of operations.
The user is prompted to select an operation by entering a number corresponding to their choice (1-10).
For operations that require two numbers (addition, subtraction, multiplication, division, exponentiation), the user is prompted to enter two numerical values.
For operations involving a single input (square root, sine, cosine, tangent, logarithm), the user is prompted to enter one numerical value.
The result of the chosen operation is then calculated and displayed.

Input Handling:

Choice Validation: The program checks if the user's choice corresponds to a valid operation (1-10). If the input is invalid, an error message is displayed.

Error Handling:

Division by Zero: The program checks for division by zero and displays an error message if the user attempts it.
Square Root of Negative Numbers: The program prevents calculating the square root of a negative number, displaying an error message instead.
Logarithm of Non-Positive Numbers: The program ensures the logarithm is only calculated for positive numbers, with error handling for non-positive inputs.

Mathematical Functions Used:

The program uses Python’s math module to perform operations like square root, sine, cosine, tangent, and logarithm.
The math.radians() function is used to convert angles from degrees to radians for trigonometric functions.

Execution:

The calculator() function encapsulates all functionality and is called at the end to run the program.

This program serves as a basic yet comprehensive calculator, allowing users to perform a variety of mathematical operations directly through a simple command-line interface.


TASK 3: PASSWORD GENERATOR

Purpose:

This Python program generates a random password based on user-defined preferences, such as length and the inclusion of uppercase letters, digits, and special characters.

Core Features:

Password Generation:

Character Set Customization:
Lowercase Letters: Always included in the password.
Uppercase Letters: Optional, based on user preference.
Digits: Optional, based on user preference.
Special Characters: Optional, based on user preference.
Random Selection:
The program randomly selects characters from the customized character set to create a password of the desired length.

User Preferences:

The program prompts the user to provide input regarding:
Password Length: The user specifies how many characters the password should contain.
Inclusion of Uppercase Letters: The user decides whether to include uppercase letters in the password.
Inclusion of Digits: The user decides whether to include numbers.
Inclusion of Special Characters: The user decides whether to include special symbols like !, @, #, etc.

Input Handling:

Password Length:

The program validates the length input to ensure it is a positive integer.
If the input is invalid (non-numeric or negative), the program prompts the user to re-enter a valid number.

Boolean Preferences:

User inputs for including uppercase letters, digits, and special characters are interpreted as yes or no.
These preferences are converted into Boolean values (True or False).

Password Output:

After generating the password based on the user's preferences, the program displays the generated password to the user.

Modular Design:

generate_password(length, use_uppercase, use_digits, use_special):
This function handles the actual generation of the password based on the specified parameters.

get_user_preferences():

This function handles user input, gathering preferences regarding password length and character types.

main():

The main function orchestrates the program flow, calling the appropriate functions to gather user input, generate the password, and display the result.

Execution:

The program is executed by running the main() function, which drives the entire process from user input to password generation and output.

Summary:

This program allows users to generate a random password that meets specific criteria. The user can control the length and complexity of the password by choosing whether to include uppercase letters, digits, and special characters. The program ensures that the password meets the specified requirements and provides a simple command-line interface for user interaction.


TASK 5: CONTACT BOOK

Purpose:

This Python program provides a simple, user-friendly system for managing a list of contacts. Users can add, view, search, update, and delete contacts, with validation checks to ensure data integrity.

Core Features:

Contact Information Storage:

Contacts are stored in a list (contacts), with each contact represented as a dictionary containing:
Name: The contact's name.
Phone: A 10-digit phone number.
Email: The contact's email address.
Address: The contact's address, limited to 40 words.

Add Contact:

Functionality: Allows users to add a new contact.
Validation:
Duplicate Name: Checks if a contact with the same name already exists. If so, it prompts the user to enter a different name.
Phone Number: Ensures the phone number is exactly 10 digits long. Non-numeric or incorrect length entries are rejected.
Address: Validates that the address does not exceed 40 words. Longer addresses are not accepted.

View Contacts:

Functionality: Displays a list of all saved contacts, showing each contact's name and phone number.
Handling:
If no contacts are saved, it informs the user that the contact list is empty.

Search Contact:

Functionality: Allows users to search for contacts by name or phone number.

Search Results:

If matching contacts are found, the program displays their details (name, phone, email, address).
If no match is found, it informs the user.

Update Contact:

Functionality: Enables users to update the details of an existing contact.

Validation:

Prevents updating to an existing contact name (avoids duplicates).
Ensures that the new phone number, if provided, is 10 digits long.
Validates that the new address, if provided, does not exceed 40 words.

Delete Contact:

Functionality: Provides the option to delete a contact by searching for it by name or phone number.

Handling:
If the contact is found, it is removed from the list.
If the contact is not found, the user is informed.

User Interface:

Main Menu:
The program offers a text-based menu that allows users to select from six options:
Add Contact
View Contacts
Search Contact
Update Contact
Delete Contact
Exit

Input Handling:

The program continually prompts the user to select an option until they choose to exit.
Program Execution:

main() Function:

Drives the entire user interface, managing the user's interaction with the contact management system.
Exit Option: The program terminates gracefully when the user chooses to exit.

Summary:

This contact management system provides a simple, easy-to-use interface for managing personal or professional contacts. It includes essential features such as adding, viewing, searching, updating, and deleting contacts, with input validation to ensure the integrity of the stored data. The program is designed to handle common issues like duplicate entries and incorrect data formats, making it robust and user-friendly.







