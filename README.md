# Library Management System

The project will be implemented using Python, a popular programming
language known for its simplicity and ease of use. The library management
system will be designed to store and manage data about books, members,
and transactions. It will also provide features such as search, filter, and sort to
allow library staff to easily access and retrieve information.
One of the key features of the project is the integration of a mail and fine
payment system. The system will be able to send automated email
notifications to members regarding due dates, overdue books, and fine
payments. It will also provide a secure online platform for members to pay
their fines using their credit or debit cards.

1. Our project is based on library management system. When you run main
file, you will see login screen. You need to select your role like admin or
student.
2. If you selected admin, you will have to enter your admin password. If you
selected student you will see three option
    1. **Signup**: Enter username email and password to sign up and verify
    your email by entering otp sent to your email address
    2. **Login**: Enter your username and password
    3. **Reset password**: verify your email and reset your password

## Menu for Admin

1. **Issue Books**: the “issue book” function takes book ID and student ID,
marks the book as issued to the student in the database, sends an
email to the student with the details of the book they have borrowed,
and displays a confirmation message.
2. **Return Book**: the “return” function takes book ID, validates it, update
database and send email to student.
3. **Search Book**: The "search book" functionality allows the user to search
for a book and display its availability status. If the book is not found, an
error message is displayed.
4. **List Books:** The "list books" functionality displays a table showing book
details and availability status for all books in the library's database.
5. **Add Book:** The "add book" functionality allows the user to add a new
book to the library's database either by entering the ISBN number or
fetching data about the book or by directly entering the book's details.
6. **Edit Book:** The "edit book" functionality allows the user to modify the
details of a book in the database by entering the book's ID or name and
updating the book's record in the database.
7. **Delete Book**: The "delete book" functionality allows the user to delete a
book from the library's database by specifying the book's ID.
8. **Student Info**: The "student info" functionality allows the user to view
information about a specific student, such as their username, email,
and total payable fine.

## Menu For Student

1. **Check Availability**: The "check availability" functionality in a menu-driven program allows the user to check the availability of a specific
book in the library's database.
2. **Reserve A Book**: The "reserve a book" functionality in a menu-driven
program allows the user to place a hold on a book that is currently
available.
3. **Update E-Mail**: The "update email" functionality allows the user to
update their email address in the system by entering their username,
new email address and verifying the OTP sent to the new email.
4. **Receive Library Card**: The "receive library card" functionality in a menu-driven program allows the user to generate a PDF library card with their
personal information, such as their username, name, and email.
5. **Pay Fine**: The "pay fine" functionality allows the user to pay their
outstanding fines using the Cashfree API. To implement this
functionality, the program might redirect the user to the CashFree
payment link, where they can enter their payment details and complete
the transaction. The Payment can be done in any methods like UPI,
Debit-Cards etc. The program should then update the user's account in
the database to reflect the paid fine.


## Table Schema

```sql
CREATE TABLE BOOKS (ID INTEGER PRIMARY KEY UNIQUE NOT NULL, TITLE CHAR NOT NULL, AUTHOR CHAR NOT NULL, PRICE NUMERIC NOT NULL, ISSUED_TO INTEGER DEFAULT (0), ISSUE_DATE DATE, RESERVED INTEGER DEFAULT (0))
```

```sql
CREATE TABLE ACCOUNTS (ID INTEGER PRIMARY KEY AUTOINCREMENT, TYPE VARCHAR (1), USERNAME VARCHAR (20), PASSWORD VARCHAR (64), AMMOUNT NUMERIC DEFAULT (0), EMAIL CHAR (32), LINKID CHAR)
```

## Screenshots
Home Screen

![home](https://github.com/user-attachments/assets/df72cd05-7ee4-4734-979f-f58635c20077)

Admin Screen

![admin](https://github.com/user-attachments/assets/db8c9721-56d1-40d7-a43c-f90e706663bf)

Student Screen

![student](https://github.com/user-attachments/assets/3622e15b-1f5f-4323-b22c-4872ac957218)

