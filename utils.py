import re
from fpdf import FPDF
import requests
from db import mycur, mydb
from rich.console import Console
from rich import print

console = Console()

def check_email(s):
    pat = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
    if re.match(pat,s):
        return True
    else:
        return False

def generate_pdf(name,username,email):
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Arial", size = 25)
    pdf.cell(200, 10, txt = "LIPS LIBRARY",
             ln = 1, align = 'C')
    pdf.cell(200, 20, txt = "STUDENT LIBRARY CARD",
             ln = 1, align = 'C')
    pdf.cell(10, 20, txt = "NAME : "+name,
             ln = 2, align = 'L')
    pdf.cell(10, 20, txt = "USERNAME :"+username,
             ln = 2, align = 'L')
    pdf.cell(10, 20, txt = "EMAIL :"+email,
             ln = 2, align = 'L')
    pdf.output("Library Card.pdf")

def generate_payment(number,linkid, ammount, note):
    url = "https://sandbox.cashfree.com/pg/links"

    payload = {
    "customer_details": {"customer_phone": number},
    "link_notify": {
        "send_email": False,
        "send_sms": False
    },
    "link_id": linkid,
    "link_amount": ammount,
    "link_currency": "INR",
    "link_purpose": note
    }
    headers = {
    "accept": "application/json",
    "x-client-id": "YOUR-CLIENT-ID",
    "x-client-secret": "YOUR-SECRET-KEY",
    "x-api-version": "2022-09-01",
    "content-type": "application/json"
    }
    response = requests.post(url, json=payload, headers=headers)
    return response.json()

def verify_payment(linkid):

    url = "https://sandbox.cashfree.com/pg/links/16698862417Aman"

    headers = {
        "accept": "application/json",
        "x-client-id": "YOUR-SECRET-KEY",
        "x-client-secret": "YOUR-SECRET-KEY",
        "x-api-version": "2022-09-01"
    }

    response = requests.get(url, headers=headers)

    return response.json()

def student_check():
    while True:
            sid = input("Enter Student ID > ")
            mycur.execute(f"SELECT * FROM ACCOUNTS WHERE ID = '{sid}' AND TYPE='S'")
            sinfo = mycur.fetchone()
            if sinfo != None:
                break
            else:
                print("[yellow bold i]Student Does Not Exists![/]")
    return sid , sinfo

def print_student(sinfo):
    print("[green]Name :", sinfo[2],"\n[green]EMail :", sinfo[5],"\n[green]Pending Amount :", sinfo[4])
def book_check():
    while True:
        id = input("Enter Book ID > ")
        if id != "exit":
            mycur.execute(f"SELECT * FROM BOOKS WHERE ID = '{id}'")
            binfo = mycur.fetchone()
            if binfo != None:
                break
            else:
                print("[yellow]Book Does Not Exists!")
        else:
            exit()
    return id, binfo


def print_book(binfo):
    print("[green]Book ID:", binfo[0],"\n[green]Title :", binfo[1],"\n[green]Author :", binfo[2],"\n[green]Price :", binfo[3])

def check_internet():
    try:
        r = requests.head('http://www.google.com/', timeout=3)
        return True
    except requests.ConnectionError as ex:
        return False
def input(text):
    return console.input("[bold cyan]"+text+"[/]")
