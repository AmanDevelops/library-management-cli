from login import login_func
import pickle, os

from rich.console import Console
console = Console()

if True:
	while True:
		try:
			f = open("data.pickle", "rb")
			data = pickle.load(f)
			break
		except:
			login_func()
	if True:
		if data[1] == "A":
			os.system("python admin.py")
		elif data[1] == "S":
			os.system("python student.py")
		try:
			f =  open("exited.dat", "rb")
			f.close()
			os.system("del exited.dat")
		except:
			pass

