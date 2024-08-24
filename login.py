import os
from db import mycur, mydb
import pickle
import hashlib
import random
from utils import check_email

os.system('cls')

def login_func():
	print("Welcome To Library Management System\n")	
	print("Select Your Option")
	print("1. Student")
	print("2. Admin")
	role = input()

	if role == "1":
		os.system('cls')
		print("Select Your Option")
		print("1. Signup")
		print("2. Login")
		print("3. Reset Password")
		ch = input("> ")
		if ch == "1":
			while True:
				uname = input("Enter Your Username : ")
				ucheck = mycur.execute(f"SELECT * FROM ACCOUNTS WHERE USERNAME = '{uname}'")
				if ucheck.fetchone() != None:
					print("Username Already Exists! Try again.")
				else:
					break
			while True:
				while True:
					eml = input("Enter New E-Mail ID")
					if check_email(eml):
						break
				echeck = mycur.execute(f"SELECT * FROM ACCOUNTS WHERE EMAIL = '{eml}'")
				if echeck.fetchone() != None:
					print("Email Already Exists! Try again.")
				else:
					break

			password = hashlib.md5(input("Enter Your password : ").encode()).hexdigest()

			mycur.execute(f"INSERT INTO ACCOUNTS (TYPE,USERNAME,PASSWORD,EMAIL) VALUES('S','{uname}','{password}','{eml}')")
			mydb.commit()
			print("Account Created Successfully! ")
			mycur.execute(f"SELECT * FROM ACCOUNTS WHERE USERNAME = '{uname}'")
			ldta = mycur.fetchone()
		if ch == "2":
			while True:
				uname = input("Enter Your Username : ")
				ucheck = mycur.execute(f"SELECT * FROM ACCOUNTS WHERE USERNAME = '{uname}'")
				if ucheck.fetchone() == None:
					print("No Username Found! Try Again")
				else:
					break
			while True:
				password = hashlib.md5(input("Enter Your password : ").encode()).hexdigest()
				mycur.execute(f"SELECT * FROM ACCOUNTS WHERE USERNAME = '{uname}' AND PASSWORD = '{password}'")
				ldta = mycur.fetchone()
				if ldta != None:
					print("Logged in Successfully!")
					break
				else:
					print("Try Again")
		if ch == "3":
			while True:
				uname = input("Enter Your Username : ")
				ucheck = mycur.execute(f"SELECT * FROM ACCOUNTS WHERE USERNAME = '{uname}'")
				sdata = ucheck.fetchone()
				if sdata == None:
					print("No Username Found! Try Again")
				else:
					break
			# code = random.randint(100000,999999)
			# send_reset(sdata[5],code,uname)

			# while True:
			# 	if int(input("Enter Your Code >> ")) == code:
			# 		password = hashlib.md5(input("Enter Your New password : ").encode()).hexdigest()
			# 		mycur.execute(f"UPDATE ACCOUNTS SET PASSWORD = '{password}' WHERE USERNAME = '{uname}'")
			# 		mydb.commit()
			# 		print("Password Changed Successfully! ")
			# 		mycur.execute(f"SELECT * FROM ACCOUNTS WHERE USERNAME = '{uname}'")
			# 		ldta = mycur.fetchone()
			# 		break
			
			password = hashlib.md5(input("Enter Your New password : ").encode()).hexdigest()
			mycur.execute(f"UPDATE ACCOUNTS SET PASSWORD = '{password}' WHERE USERNAME = '{uname}'")
			mydb.commit()
			print("Password Changed Successfully! ")
			mycur.execute(f"SELECT * FROM ACCOUNTS WHERE USERNAME = '{uname}'")
			ldta = mycur.fetchone()

						
	elif role == "2":
		os.system('cls')
		mycur.execute("SELECT * FROM ACCOUNTS WHERE TYPE = 'A'")
		ldta = mycur.fetchone()
		fpass = ldta[3]

		login = False
		while login != True:
			password = input("Enter Your password : ")
			if fpass == password:
				print("Logged in Successfully! ")
				break
			else:
				print("Auth Unsuccessfull!")
	with open("data.pickle", "wb") as f:
		pickle.dump(ldta,f)

	os.system('cls')