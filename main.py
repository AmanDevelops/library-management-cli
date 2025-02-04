import os
import pickle

from rich.console import Console

from utils.login import login_func

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
            f = open("exited.dat", "rb")
            f.close()
            os.system("del exited.dat")
        except:
            pass
