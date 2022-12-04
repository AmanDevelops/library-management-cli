import os, smtplib,ssl, random
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText


email_id = "YOUR-EMAIL@YOUR-DOMAIN.COM"
email_pass = "EMAIL-PASSWORD"

def send_reg(receiver_email,username,id):

    with smtplib.SMTP('SMTP.YOUR-DOMAIN.COM',587) as smtp:
        smtp.starttls()
        smtp.ehlo()
        smtp.login(email_id,email_pass)
        subject = "Registration Successful - LIPS Library"
        body = f"""\
You Have Successfully registered to LIPS Library Management System.\n
Student ID: {id}\n
Username : {username}\n
E-Mail: {receiver_email}\n
Thank You."""
        msg = f"Subject: {subject}\n\n\n{body}"
        smtp.sendmail(email_id,receiver_email,  msg)
def send_reset(receiver_email,code, username):
    with smtplib.SMTP('SMTP.YOUR-DOMAIN.COM',587) as smtp:
        smtp.starttls()
        smtp.ehlo()
        smtp.login(email_id,email_pass)
        subject = "Your Reset Code is "+code+" - LIPS Library"
        body = f"""\
Dear {username}\n
Your Password Reset Code is {code}\n
Thank You."""
        msg = f"Subject: {subject}\n\n\n{body}"
        smtp.sendmail(email_id,receiver_email,  msg)
def send_verify(receiver_email,code, username):
    with smtplib.SMTP('SMTP.YOUR-DOMAIN.COM',587) as smtp:
        smtp.starttls()
        smtp.ehlo()
        smtp.login(email_id,email_pass)
        subject = "Your Reset Code is {code} - LIPS Library"
        body = f"""\
Dear {username}\n
Your Password Reset Code is {code}\n
Thank You."""
        msg = f"Subject: {subject}\n\n\n{body}"
        smtp.sendmail(email_id,receiver_email,  msg)
def send_issue(receiver_email, book_id, book_title,author, return_date, username):
    with smtplib.SMTP('SMTP.YOUR-DOMAIN.COM',587) as smtp:
        smtp.starttls()
        smtp.ehlo()
        smtp.login(email_id,email_pass)
        subject = "Your Book has been issued - LIPS Library"
        body = f"""\
Dear {username}\n
Your Book has been issued.\n
Book ID: {book_id}\n
Book Title: {book_title}\n
Book Author: {author}\n
Your Last Date to return this book is {return_date}.\n
Thank You."""
        msg = f"Subject: {subject}\n\n\n{body}"
        smtp.sendmail(email_id,receiver_email,  msg)
def send_ret(receiver_email, book_id, book_title,author, return_date, username, fine, fine2):
    with smtplib.SMTP('SMTP.YOUR-DOMAIN.COM',587) as smtp:
        smtp.starttls()
        smtp.ehlo()
        smtp.login(email_id,email_pass)
        subject = "Your Book has been Returned - LIPS Library"
        body = f"""\
Dear {username}\n
Your Book has been returned on {return_date}.\n
Your Total Payable Fine is Rs. {fine}
Your Fine on this book is {fine2}\n
Book Details:
Book ID: {book_id}
Book Title: {book_title}
Book Author: {author}
Thank You."""
        msg = f"Subject: {subject}\n\n\n{body}"
        smtp.sendmail(email_id,receiver_email,  msg)
def send_payment(receiver_email, username, fine,link):
    with smtplib.SMTP('SMTP.YOUR-DOMAIN.COM',587) as smtp:
        smtp.starttls()
        smtp.ehlo()
        smtp.login(email_id,email_pass)
        subject = "Your Fine Payment Link - LIPS Library"
        body = f"""\
Dear {username}\n
To Pay Your Fine, \n
Step 1 : Visit this Link And Pay\n
{link}\n
Step 2 : Verify Your Payment From Second Option On Payment's Menu\n
Thank You"""
        msg = f"Subject: {subject}\n\n\n{body}"
        smtp.sendmail(email_id,receiver_email,  msg)
