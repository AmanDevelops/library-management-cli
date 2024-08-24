from db import mycur,mydb
import os, time
from prettytable import PrettyTable
from rich.table import Table
import datetime
from mail import *
from utils import *
from rich.console import Console
from rich import print
from rich.prompt import Prompt

console = Console()


os.system('cls')
print()
print()
console.print("[red]LIPS Library Management System[/red]", justify="center",)


print("Select an option")
print("1. [green]Issue Book")
print("2. [green]Return Book")
print("3. [green]Search Book")
print("4. [green]List Books")
print("5. [green]Add Book")
print("6. [green]Edit Book")
print("7. [green]Delete Book")
print("8. [green]Student Info")
print("9. [green]Exit")

ch = input("Enter >>")

if ch == "1":
	while True:
		sid, sinfo = student_check()
		print_student(sinfo)
		while True:
			id,binfo = book_check()
			if mycur.execute(f"SELECT * FROM BOOKS WHERE ID = '{id}' AND ISSUED_TO = 0").fetchone() != None: 
				print_book(binfo)
				if binfo[6] != 0:
					print("[yellow]This Book is Reserved by Someone![/]")
				chch = input("Do You want To Issue This book [red](yes/no)[/] > ")
				if chch.lower() not in ("n", "nn", "not"):
					today = datetime.date.today()
					mycur.execute(f"UPDATE BOOKS SET ISSUED_TO = {sid}, ISSUE_DATE = '{today}', RESERVED = 0 WHERE ID = {id}")
					mydb.commit()
					print("[green]The Book Has been Issued to [/]",sinfo[2])
					if check_internet():
						with console.status("[bold green]Sending Email...") as status:
							return_date = (today+datetime.timedelta(days=15)).strftime('%A %d %B %Y')
					else:
						print("[red]Not Connected To Internet[/]")
				break
			else:
				print("[red]The Book is not available[/]")
		if input("Want to issue More? [red](y/n)[/]") in ("n", "nn", "not"):
			break
elif ch == "2":
	while True:
		id,binfo = book_check()
		if mycur.execute(f"SELECT * FROM BOOKS WHERE ID = '{id}'").fetchone()[4] != 0: 
			print_book(binfo)
			chch = input("Do You want To Return This book [red](y/n)[/] >> ")
			if chch.lower() not in ("n", "nn", "not"):
				idate = datetime.datetime.strptime(binfo[5], '%Y-%m-%d')
				cdate = datetime.datetime.strptime(str(datetime.date.today()), '%Y-%m-%d')
				days = (cdate-idate).days
				if days >= 15:
					fine = (days-15)*3
				else:
					fine = 0
				mycur.execute(f"UPDATE BOOKS SET ISSUED_TO = 0 , ISSUE_DATE = NULL WHERE ID = '{id}'")
				mydb.commit()
				mycur.execute(f"UPDATE ACCOUNTS SET AMMOUNT = AMMOUNT + {fine} WHERE ID = {binfo[4]}")
				mydb.commit()
				sinfo = mycur.execute(f"SELECT * FROM ACCOUNTS WHERE ID = {binfo[4]}").fetchone()
				print("[green]Book has Been Returned!")
		else:
			print("[yellow]The Book is not Issued")
		if input("Want to return More[red](y/n)[/]") in ("n", "nn", "not"):
			break
elif ch == "3":
	id,binfo = book_check()
	print_book(binfo)
	if binfo[4] != 0:
			mycur.execute(f"SELECT * FROM ACCOUNTS WHERE ID = {binfo[4]}")
			name = mycur.fetchone()[2]
			print("[green]Issued To:", name,"\n[green]Issued on:",binfo[5])
	else:
		print("[green]Not Issued[/]")
elif ch == "4":
	table = Table(show_header=True, header_style="bold magenta")
	table.add_column("ID", style="dim", width=12)
	table.add_column("Title")
	table.add_column("Author", justify="right")
	table.add_column("Price", justify="right")
	table.add_column("Issued To", justify="right")
	table.add_column("Issued Date", justify="right")


	#x = PrettyTable()
	#x.field_names = ["ID", "Title", "Author", "Price","Issued To", "Issue Date"]
	mycur.execute("SELECT * FROM BOOKS")
	data = mycur.fetchall()
	for i in data:
		if i[4] != 0:
			mycur.execute(f"SELECT * FROM ACCOUNTS WHERE ID = {i[4]}")
			name = mycur.fetchone()[2]
		else:
			name = "Not Issued"
		#x.add_row([i[0], i[1], i[2], i[3], name, i[5]])
		table.add_row("[cyan]"+str(i[0]), "[green]"+str(i[1]), "[green]"+str(i[2]), "[green]"+str(i[3]), "[green]"+name, "[green]"+str(i[5]))
	console.print(table)

elif ch == "5":
	while True:
		while True:
			id = input("Enter Book ID > ")
			mycur.execute("SELECT * FROM BOOKS WHERE ID = '{id}'")
			if mycur.fetchone() == None:
				break

		title = input("Enter Book Title > ")
		author = input("Enter Book Author > ")
		price = input("Enter Book price > ")

		mycur.execute(f"INSERT INTO BOOKS (ID,TITLE,AUTHOR,PRICE) VALUES ({id}, '{title}','{author}',{price})")
		mydb.commit()
		print("[green]Book Added Successfully! ")
		time.sleep(2)
		if input("Do You Want to Add More ? [red](y/n)[/]").lower() in ("n", "nn", "not"):
			break
elif ch == "6":
	id,binfo = book_check()
	print_book(binfo)
	while True:
		print("[green]What do you want to edit? \n")
		print("[green][cyan]1.[/] Book ID\n[cyan]2.[/] Title \n[cyan]3.[/] Author \n[cyan]4.[/] Price[/]")
		chch = input("")
		if chch in ("1","2","3","4"):
			if chch == "1":
				while True:
					nid = input("Enter New Book ID > ")
					mycur.execute(f"SELECT * FROM BOOKS WHERE ID = '{nid}'")
					binfo = mycur.fetchone()
					if binfo == None:
						break
					else:
						print("[yellow]Book already Assigned With this ID[/]")
					
				mycur.execute(f"UPDATE BOOKS SET ID = {nid} WHERE ID = {id}")
			elif chch == "2":
				ntitle = input("Enter New Book Title > ")
				mycur.execute(f"UPDATE BOOKS SET TITLE = '{ntitle}' WHERE ID = {id}")
			elif chch == "3":
				nauthor = input("Enter New Author > ")
				mycur.execute(f"UPDATE BOOKS SET AUTHOR = '{nauthor}' WHERE ID = {id}")
			elif chch == "4":
				nprice = input("Enter New Price > ")
				mycur.execute(f"UPDATE BOOKS SET PRICE = {nprice} WHERE ID = {id}")
			mydb.commit()
			print("[green]Book's Data Successfully Updated! ")
			time.sleep(2)
			if input("Do You want to edit more? [red](y/n)[/]").lower() in ("n", "nn", "not"):
				break
		
elif ch == "7":
	while True:
		id,binfo = book_check()
		print_book(binfo)
		if input('[red bold]Are you sure you want to delete this book? type [green]"yes"[/] >> [/]').lower() == "yes":
			mycur.execute(f"DELETE FROM BOOKS WHERE ID = {id}")
			mydb.commit()
			print("[red]Book Deleted Successfully!")
			time.sleep(2)
		if input("Do You Want To Delete More ? [red](y/n)") in ("n", "nn", "not"):
			break
if ch == "8":
	sid, sinfo = student_check()
	print_student(sinfo)
		