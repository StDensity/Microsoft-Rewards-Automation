
import os


class AutoSearch:
    def __init__(self):
        pass



    def start_run(self, window):
        self.update_entry_values(window)

        # Disables Start button to prevent multiple clicks.
        window.start_button['state'] = 'disabled'

        # Disable Browser Close Check box
        window.browser_close_checkbox.config(state="disabled")

    def do_search(self):
        path = path = "C:\\Program Files (x86)\\Microsoft\\Edge\\Application\\msedge.exe"

    def update_entry_values(self, window):
        self.browser_open_delay = float(window.browser_open_delay_entry.get())
        self.inspect_element_delay = float(window.inspect_element_delay_entry.get())
        self.search_delay = float(window.search_delay_entry.get())
        self.total_searches = int(window.total_searches_entry.get())

    def save_config(self):
        pass

    def reset_config(self):
        pass

    @staticmethod
    def close_app(window):
        window.destroy()
