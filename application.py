from tkinter import *

from encrypt import CaesarCypher as CaesarCypherEncrypt
from decrypt import CaesarCypher as CaesarCypherDecrypt
from decrypt import VernamCypher as VernamCypherDecrypt
from encrypt import VernamCypher as VernamCypherEncrypt


# Create Root Window
root = Tk()

# Basic Settings
root.title("Encryption Application")
root.geometry("500x500")


# Run it all
root.mainloop()
