import tkinter as tk
from tkinter import ttk


class Gui(tk.Tk):
    def __init__(self, width, height, auto_search):
        super().__init__()

        self.auto_search = auto_search
        self.title("Auto Search Tool")
        self.geometry(f"{width}x{height}")
        self.minsize(500, 300)
        self.main = None
        self.setup_ui()

        self.mainloop()

    def setup_ui(self):
        self.main = Main(self.auto_search)
        self.main.pack(padx=20, pady=20, fill="both", expand=True)

        # Setting up default values
        self.main.browser_open_delay_entry.insert(0, self.auto_search.browser_open_delay)
        self.main.inspect_element_delay_entry.insert(0, str(self.auto_search.inspect_element_delay))
        self.main.search_delay_entry.insert(0, str(self.auto_search.search_delay))
        self.main.total_searches_entry.insert(0, str(self.auto_search.total_searches))


class Main(ttk.Frame):
    def __init__(self, parent):
        super().__init__()
        self.close_button = None
        self.start_button = None
        self.total_searches_entry = None
        self.total_searches_label = None
        self.search_delay_entry = None
        self.search_delay_label = None
        self.inspect_element_delay_entry = None
        self.inspect_element_delay_label = None
        self.browser_open_delay_entry = None
        self.browser_open_delay_label = None
        self.auto_search = parent
        self.setup_entry_fields()
        self.setup_buttons()

    def setup_entry_fields(self):
        self.browser_open_delay_label = ttk.Label(self, text="Browser Open Delay:")
        self.browser_open_delay_label.grid(row=0, column=0, padx=5, pady=5, sticky="w")
        self.browser_open_delay_entry = ttk.Entry(self)
        self.browser_open_delay_entry.grid(row=0, column=1, padx=5, pady=5)

        self.inspect_element_delay_label = ttk.Label(self, text="Inspect Element Delay:")
        self.inspect_element_delay_label.grid(row=1, column=0, padx=5, pady=5, sticky="w")
        self.inspect_element_delay_entry = ttk.Entry(self)
        self.inspect_element_delay_entry.grid(row=1, column=1, padx=5, pady=5)

        self.search_delay_label = ttk.Label(self, text="Search Delay:")
        self.search_delay_label.grid(row=2, column=0, padx=5, pady=5, sticky="w")
        self.search_delay_entry = ttk.Entry(self)
        self.search_delay_entry.grid(row=2, column=1, padx=5, pady=5)

        # Create and configure the Total Searches entry field
        self.total_searches_label = ttk.Label(self, text="Total Searches:")
        self.total_searches_label.grid(row=3, column=0, padx=5, pady=5, sticky="w")
        self.total_searches_entry = ttk.Entry(self)
        self.total_searches_entry.grid(row=3, column=1, padx=5, pady=5)

    def setup_buttons(self):
        # Start Button
        self.start_button = ttk.Button(self, text="Start Search", command=self.auto_search.start_search)
        self.start_button.grid(row=4, columnspan=2, pady=10)

        # Close Button
        self.close_button = ttk.Button(self, text="Close", command=self.auto_search.close_app)
        self.close_button.grid(row=5, columnspan=2, pady=10)




