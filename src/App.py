from AutoSearch import AutoSearch
from tkinter import messagebox

from Gui import Gui

try:
    if __name__ == '__main__':
        Gui(310, 300)
except Exception as e:
    messagebox.showerror("Error", f"An error occurred {e}")
