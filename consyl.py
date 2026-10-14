import sys
import getpass
import subprocess
import os
import tkinter as tk
from tkinter import messagebox
root = tk.Tk()
root.withdraw()
uname = getpass.getuser()
while True:
    command = input(f"{uname}~=")
    match command:
        case "!help":
            print("""!help-Справка
            !exit-Выход из консоли
            !fox-Открывает редактор foxtrot
            !clc-Очищает консоль
            !abo-О консоли и редакторе""")
        case "!exit":
            sys.exit(0)
        case "!fox":
            print("Foxtrot 1.0")
            break
        case "!clc":
            os.system("clear")
        case "!abo":
            print("""Консоль Consyl(1.0)
            Текстовый редактор foxtrot(1.0)
            Создатель:olegkiller
            Ссылка на репозетории github:""")
        case _:
            messagebox.showerror("Ошибка 1-001","Неизвестная команда")
        
            
