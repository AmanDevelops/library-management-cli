import os, pickle
from db import mycur,mydb
from fuzzywuzzy import fuzz
from fuzzywuzzy import process
from prettytable import PrettyTable
from utils import *
import random, time
from mail import *


os.system('cls')

print("Welcome To Library Management System\n")
print("Select an Option:")
print("1. Check Availability")
print("2. Reserve A Book")
print("3. Update E-Mail")
print("4. Recieve Library Card")
print("5. Pay Fine")
print("6. Exit")

ch = input(">")

if ch == "1":
	while True:
		id, binfo = book_check()
		print_book(binfo)
		if binfo[4] != 0: 		
			print("The Book is not available")
		else:
			print("The Book is Available")
elif ch == "2":
	while True:
		bs = input("Enter Book Name or Book ID >> ")
		if bs.isnumeric():
			binfo = mycur.execute(f"SELECT * FROM BOOKS WHERE ID = {bs}").fetchone()
			if binfo == None:
				print("Book Does Not Exists!")
		else:
			bdb = mycur.execute("SELECT * FROM BOOKS").fetchall()
			x = PrettyTable()
			x.field_names = ["ID", "Title", "Author", "Price","Issued To", "Issue Date", "Is Reserved"]
			for i in bdb:
				if fuzz.ratio(bs.lower(), i[1].lower()) > 60:
					if i[4] != 0:
						name = "Issued"
					else:
						name = "Not Issued"
					if i[6] != 0:
						nameR = "Reserved"
					else:
						nameR = "Not Reserved"
					x.add_row([i[0], i[1], i[2], i[3], name, i[5],nameR])
			if len(x.rows) == 0:
				binfo = None
				print("No Result Found")
			else:
				print(x) 
				id, binfo = book_check()
		if binfo != None:
			break
	
	print_book(binfo)
	if binfo[6] == 0:
		if binfo[4] != 0: 		
			print("The Book is not available")
		else:
			print("The Book is Available")
			with open("data.pickle", "rb") as f:
				data = pickle.load(f)
			if len(mycur.execute(f"SELECT * FROM BOOKS WHERE RESERVED = {data[0]}").fetchall()) > 2:
				print("You Reached The Maximum Limit to Issue Books")
			else:
				if input("Do You Want to Reserve This Book? (y/n)") not in ("n", "nn", "not"):
					mycur.execute(f"UPDATE BOOKS SET RESERVED = {data[0]} WHERE ID = {binfo[0]}")
					mydb.commit()
					print("Your Book has been reserved")
	else:
		print("The Book is Already Reserved")
elif ch == "3":
	while True:
		while True:
			emailid = input("Enter New E-Mail ID")
			if emailid == "exit":
				exit()
			if check_email(emailid):
				break
		echeck = mycur.execute(f"SELECT * FROM ACCOUNTS WHERE EMAIL = '{emailid}'")
		if echeck.fetchone() != None:
			print("Email Already Exists! Try again.")
		else:
			break	
	code = random.randint(100000,999999)
	with open("data.pickle", "rb") as f:
		data = pickle.load(f)
		username = data[2]
	if check_internet():
		send_verify(emailid,code,username)
		while True:
			if input("Enter OTP > ") == str(code):
				mycur.execute(f"UPDATE ACCOUNTS SET EMAIL = '{emailid}' WHERE ID = {data[0]}")
				mydb.commit()
				print("EMail ID Updated Successfully")
				break
			else:
				print("Try Again")
	else:
		print("Please Connect To Internet")
elif ch == "4":
	with open("data.pickle", "rb") as f:
		data = pickle.load(f)
	generate_pdf(data[2],data[2], data[5])
	print("Library Card Saved on your Current Folder")

elif ch == "5":
	with open("data.pickle", "rb") as f:
		data = pickle.load(f)
	data = mycur.execute(f"SELECT * FROM ACCOUNTS WHERE ID = {data[0]}").fetchone()
	print("Your Total Fine Ammount is Rs. ", data[4])
	if data[4] > 0:
		print("Choose an Option")
		print("1. Create Payment")
		print("2. Verify Payment")
		chch = input(">>")
		if chch == "1":
			linkid = str(int(time.time()))+str(data[0])
			ammount = data[4]
			note = "Fine Payment of "+ data[2]
			if check_internet():
				print("Generating Link Please Wait...")
				data2 = generate_payment(input("Enter Mobile Number>>"), linkid,ammount,note)
				mycur.execute(f"""UPDATE ACCOUNTS SET LINKID = '{data2["link_id"]}' WHERE ID = {data[0]}""")
				mydb.commit()
				print("Sending Mail...")
				send_payment(data[5],data[2], ammount, data2["link_url"])
				print("Mail Successfully Sent!")
			else:
				print("Please Check Your Internet Connection and Try Again")
		elif chch == "2":
			linkid = mycur.execute(f"SELECT * FROM ACCOUNTS WHERE ID = {data[0]}").fetchone()[6]
			if check_internet():
				if verify_payment(linkid)["link_status"] == "PAID":
					mycur.execute(f"UPDATE ACCOUNTS SET AMMOUNT = 0, LINKID = Null WHERE ID = '{data[0]}'")
					mydb.commit()
				else:
					print("Couldn't Verify Payments")
			else:
				print("Please Check Your Internet Connection and Try Again")
elif ch == "6":
	with open("exited.dat", "wb") as f:
		pass