import tkinter as tk
from tkinter import ttk
import configparser
from AutoSearch import AutoSearch

class Gui(tk.Tk):
    def __init__(self, width, height):
        super().__init__()
        self.title("Auto Search Tool")
        self.geometry(f"{width}x{height}")
        self.minsize(310, 300)

        self.total_searches = None
        self.search_delay = None
        self.inspect_element_delay = None
        self.browser_open_delay = None
        self.browser_close_check_button = None
        self.note_label = None
        self.browser_close_checkbutton = None
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

        self.get_config_data()
        self.setup_ui()

        self.mainloop()

    def setup_ui(self):
        self.setup_main_page()

        # Setting up default values
        self.browser_open_delay_entry.insert(0, str(self.browser_open_delay))
        self.inspect_element_delay_entry.insert(0, str(self.inspect_element_delay))
        self.search_delay_entry.insert(0, str(self.search_delay))
        self.total_searches_entry.insert(0, str(self.total_searches))

    def setup_main_page(self):
        frame = ttk.Frame()
        frame.pack(padx=20, pady=20, fill="both", expand=True)
        self.browser_open_delay_label = ttk.Label(frame, text="Browser Open Delay:")
        self.browser_open_delay_label.grid(row=0, column=0, padx=5, pady=5, sticky="w")
        self.browser_open_delay_entry = ttk.Entry(frame)
        self.browser_open_delay_entry.grid(row=0, column=1, padx=5, pady=5)

        self.inspect_element_delay_label = ttk.Label(frame, text="Inspect Element Delay:")
        self.inspect_element_delay_label.grid(row=1, column=0, padx=5, pady=5, sticky="w")
        self.inspect_element_delay_entry = ttk.Entry(frame)
        self.inspect_element_delay_entry.grid(row=1, column=1, padx=5, pady=5)

        self.search_delay_label = ttk.Label(frame, text="Search Delay:")
        self.search_delay_label.grid(row=2, column=0, padx=5, pady=5, sticky="w")
        self.search_delay_entry = ttk.Entry(frame)
        self.search_delay_entry.grid(row=2, column=1, padx=5, pady=5)

        # Create and configure the Total Searches entry field
        self.total_searches_label = ttk.Label(frame, text="Total Searches:")
        self.total_searches_label.grid(row=3, column=0, padx=5, pady=5, sticky="w")
        self.total_searches_entry = ttk.Entry(frame)
        self.total_searches_entry.grid(row=3, column=1, padx=5, pady=5)

        # Start Button
        self.start_button = ttk.Button(frame, text="Start Search", command=self.start_run)
        self.start_button.grid(row=4, columnspan=2, pady=10)

        # Close Button
        self.close_button = ttk.Button(frame, text="Close", command=self.close_app)
        self.close_button.grid(row=5, columnspan=2, pady=10)

        # Check Button
        # It's variable need to be initialized as tkinter IntVar object for proper working.
        self.browser_close_check_button = tk.IntVar()

        self.browser_close_checkbutton = ttk.Checkbutton(frame, text="Close browser on completion",
                                                         variable=self.browser_close_check_button)
        self.browser_close_checkbutton.grid(row=6, columnspan=2, padx=10)

        # Note Label
        self.note_label = ttk.Label(frame, text="Made with ❤")
        self.note_label.grid(row=7, columnspan=2, pady=10)


    def get_config_data(self):
        config = configparser.ConfigParser()

        config.read('../config.ini')

        self.browser_open_delay = config.get('default_values', 'browser_open_delay')
        self.inspect_element_delay = config.get('default_values', 'inspect_element_delay')
        self.search_delay = config.get('default_values', 'search_delay')
        self.total_searches = config.get('default_values', 'total_searches')

    def start_run(self):
        self.update_entry_values()

        # Disables Start button to prevent multiple clicks.
        self.start_button['state'] = 'disabled'

        # Disable Browser Close Check box
        self.browser_close_checkbutton.config(state="disabled")

    def close_app(self):
        self.destroy()

    def update_entry_values(self):
        self.browser_open_delay = float(self.browser_open_delay_entry.get())
        self.inspect_element_delay = float(self.inspect_element_delay_entry.get())
        self.search_delay = float(self.search_delay_entry.get())
        self.total_searches = int(self.total_searches_entry.get())
