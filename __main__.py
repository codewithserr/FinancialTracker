import tkinter as tk
from tkinter import filedialog

# Import modules from src folder
import src.guy as guy
import src.database as db

# Create the database in case it does not exists
db.createDatabase()

root = tk.Tk()
app = guy.FinanceTracker(root)
root.mainloop()

