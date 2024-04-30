from Singleton import Singleton
import os
import time
import ctypes
import json
import pyautogui as auto
import random


@Singleton
class AutoSearch:
    def __init__(self):
        self.search_terms = None
        self.prefix = None
        self.root = None
        self.required_browser_id = None

    def start_search(self, root):
        self.root = root
        path = "C:\\Program Files (x86)\\Microsoft\\Edge\\Application\\msedge.exe"
        # An exception is raised if the browser is not found.
        try:
            # Open Microsoft Edge Canary using the specified shortcut
            os.startfile(path)
        except FileNotFoundError as e:
            root.show_alert("Browser Not Found", "Please ensure that edge is installed in: \n" + path)
            return
        except Exception as e:
            root.show_alert("Error", "An error occurred while opening the browser. Error code: " + str(e))

        # Pause the script execution for the specified browser open delay
        time.sleep(self.root.browser_open_delay)

        # Getting the ID of the active window, it should be a browser.
        self.required_browser_id = ctypes.windll.user32.GetForegroundWindow()

        data = self.load_search_keys()

        self.prefix = data['prefix']
        self.search_terms = data['search_terms']
        self.check_focus()

        self.search_loop()

    def search_loop(self):
        for i in range(0, self.root.total_searches):
            self.check_focus()
            auto.hotkey('ctrl', 'l')

            # Generate a random question by choosing a random prefix and search_terms
            auto.typewrite(random.choice(self.prefix) + " ")
            time.sleep(1)
            auto.typewrite(random.choice(self.search_terms))
            auto.press("enter")  # Press the "enter" key
            time.sleep(self.root.search_delay)  # Pause for the specified search delay

        self.check_focus()
        if self.root.browser_close_check_var.get():  # We need to use .get() here to get the checkbox true value.
            self.close_browser()
        else:
            # To go to the Rewards site.
            auto.hotkey('ctrl', 'l')
            auto.typewrite("https://rewards.bing.com/")
            auto.press("enter")

    @staticmethod
    def load_search_keys():

        with open('../Resources/search_keys.json', 'r') as f:
            data = json.load(f)

        return data

    @staticmethod
    def close_browser():
        # ctrl + shift + w closes the active browser window
        auto.hotkey('ctrl', 'shift', 'w')

    def check_focus(self):
        current_window = ctypes.windll.user32.GetForegroundWindow()
        if self.required_browser_id != current_window:
            self.root.show_alert("Error", "Browser focus lost. Exit(0)")
            exit(0)