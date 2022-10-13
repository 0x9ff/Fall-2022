from colorama import Fore, Back, Style

print(Back.YELLOW + "Hi, this is a project for PyCharm. It has several libraries preinstalled." + Style.RESET_ALL)
print("When making a new python file, make sure to right-click on the \"Fall 2022\" folder\n"
      "or other project sub-folder and then select New->File.\n"
      "Then name the file something with .py as the extension.")
print(Fore.RED + Style.BRIGHT + "NOTE: Do *NOT* right-click on the \"venv\" folder when making a new file."
      + Style.RESET_ALL)
print()
print("To run a project for the first time, right click on the file and select Run.")
print("To run a project again, you can just hit the play button at the top or hit CTRL-R.")
print(Fore.BLUE + "Note: the drop-down menu to the left of the play button says the current file that will run."
      + Style.RESET_ALL)