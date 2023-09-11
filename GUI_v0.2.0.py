import tkinter as tk
from tkinter import messagebox
from tkinter import ttk
import pyautogui as auto
import time
import random
import os
import pygetwindow as gw

# Create the main application window
root = tk.Tk()
root.title("Auto Search Tool")
root.geometry("500x300")  # Set the window size

# Create a frame to organize widgets
frame = ttk.Frame(root)
frame.pack(padx=20, pady=20, fill="both", expand=True)


# Function to start the search
def start_search():
    global browser_open_delay, inspect_element_delay, search_delay, total_searches

    # Get user-defined delay values from entry fields
    browser_open_delay = float(browser_open_delay_entry.get())
    inspect_element_delay = float(inspect_element_delay_entry.get())
    search_delay = float(search_delay_entry.get())
    total_searches = int(total_searches_entry.get())

    # Disable the Start button to prevent multiple clicks
    start_button['state'] = 'disabled'

    # Disable Browser Close Check box
    browser_close_checkbox.config(state="disabled")

    # Call the execute_search function
    execute_search(total_searches, browser_open_delay, inspect_element_delay, search_delay)


# Function to close the application
def close_app():
    root.destroy()
    exit(0)

def close_browser():
    # ctrl + shift + w closes the active browser window
    auto.hotkey('ctrl', 'shift', 'w')

def show_alert(title, message):
    messagebox.showinfo(title, message)


def check_focus(required_window_id):
    active_window_list_2 = gw.getWindowsWithTitle(gw.getActiveWindow().title)
    current_browser = active_window_list_2[0]._hWnd
    if required_window_id != current_browser:
        show_alert("Error", "Browser focus lost. Exit(0)")
        exit(0)


# Default delay values
browser_open_delay = 5
inspect_element_delay = 5
search_delay = 2
total_searches = 70  # Initialize total_searches variable

# Create and configure entry fields for delay values
browser_open_delay_label = ttk.Label(frame, text="Browser Open Delay:")
browser_open_delay_label.grid(row=0, column=0, padx=5, pady=5, sticky="w")
browser_open_delay_entry = ttk.Entry(frame)
browser_open_delay_entry.grid(row=0, column=1, padx=5, pady=5)
browser_open_delay_entry.insert(0, str(browser_open_delay))  # Set default value

inspect_element_delay_label = ttk.Label(frame, text="Inspect Element Delay:")
inspect_element_delay_label.grid(row=1, column=0, padx=5, pady=5, sticky="w")
inspect_element_delay_entry = ttk.Entry(frame)
inspect_element_delay_entry.grid(row=1, column=1, padx=5, pady=5)
inspect_element_delay_entry.insert(0, str(inspect_element_delay))  # Set default value

search_delay_label = ttk.Label(frame, text="Search Delay:")
search_delay_label.grid(row=2, column=0, padx=5, pady=5, sticky="w")
search_delay_entry = ttk.Entry(frame)
search_delay_entry.grid(row=2, column=1, padx=5, pady=5)
search_delay_entry.insert(0, str(search_delay))  # Set default value

# Create and configure the Total Searches entry field
total_searches_label = ttk.Label(frame, text="Total Searches:")
total_searches_label.grid(row=3, column=0, padx=5, pady=5, sticky="w")
total_searches_entry = ttk.Entry(frame)
total_searches_entry.grid(row=3, column=1, padx=5, pady=5)
total_searches_entry.insert(0, str(total_searches))  # Set default value

# Create and configure the Start button
start_button = ttk.Button(frame, text="Start Search", command=start_search)
start_button.grid(row=4, columnspan=2, pady=10)

# Create and configure the Close button
close_button = ttk.Button(frame, text="Close", command=close_app)
close_button.grid(row=5, columnspan=2, pady=10)

# Browser close check box.
browser_close_var = tk.IntVar()
browser_close_checkbox = ttk.Checkbutton(frame, text="Close browser on completion", variable=browser_close_var)
browser_close_checkbox.grid(row=6, columnspan=2, padx=10)

note_label = ttk.Label(frame, text="Note: The total number of searches will be halved for both PC and mobile searches.")
note_label.grid(row=7, columnspan=2, pady=10)


# Function to execute the search
def execute_search(total_searches, browser_open_delay, inspect_element_delay, search_delay):
    # Define the path to the Microsoft Edge
    # Put the path in a file called path.txt in the same directory.
    # path_file = open('path.txt', 'r')
    # browser_path = path_file.read()

    path = "C:\\Program Files (x86)\\Microsoft\\Edge\\Application\\msedge.exe"

    # Open Microsoft Edge Canary using the specified shortcut
    os.startfile(path)

    # Pause the script execution for the specified browser open delay
    time.sleep(browser_open_delay)

    # Getting the ID of the active window.
    active_window_list = gw.getWindowsWithTitle(gw.getActiveWindow().title)
    required_window_id = active_window_list[0]._hWnd

    # Define a list of prefixes to be used in generating questions
    prefix = [
        "What is", "Define", "Explain", "Meaning of",
        "WOverview of RNN"
        "hat are", "Characteristics of", "Importance of", "Advantages of",
        "Disadvantages of", "Types of", "Function of", "History of", "Principles of",
        "Components of", "Role of", "Purpose of", "Benefits of", "Concept of",
        "Process of", "Techniques of", "Applications of", "Definition of", "Theory of",
        "Overview of", "Challenges of", "Significance of", "Structure of", "Scope of",
        "Framework of", "Objectives of", "Methods of", "Features of", "Classification of"
    ]

    # Define a list of words related to AI and machine learning
    words = [
        "AI", "ANN", "CNN", "RNN", "NLP", "GAN", "SVM", "PCA",
        "IoT", "AIOps", "RL", "ELMo", "BERT", "LSTM", "GRU",
        "K-means", "FNN", "Transfer Learning", "AutoML",
        "Hyperparameter Optimization", "Reinforcement Learning",
        "Deep Learning", "Regression Analysis", "Clustering",
        "Dimensionality Reduction", "Backpropagation", "Over fitting",
        "Under fitting", "Cross-Validation", "Natural Language Generation",
        "Supervised Learning", "Unsupervised Learning", "Neural Network Architecture",
        "Bias-Variance Tradeoff", "Feature Engineering", "Convolutional Neural Network",
        "Recurrent Neural Network", "Random Forest", "Gradient Descent"
    ]

    # To check whether the browser has lost focus or not.
    check_focus(required_window_id)

    # Opens Inspect Elements
    auto.hotkey('ctrl', 'shift', 'i')
    time.sleep(inspect_element_delay)
    # To check whether the browser has lost focus or not.
    check_focus(required_window_id)
    # This is the bring back focus to the browser from inspect elements
    auto.hotkey('alt')

    # Loop to automate a series of actions
    for i in range(0, total_searches):
        # To check whether the browser has lost focus or not.
        check_focus(required_window_id)
        if i == total_searches // 2:
            # Toggles device mode
            auto.hotkey('ctrl', 'shift', 'i')
            time.sleep(inspect_element_delay)
            auto.hotkey('ctrl', 'shift', 'i')
            time.sleep(inspect_element_delay)
            auto.hotkey('ctrl', 'shift', 'm')
            time.sleep(inspect_element_delay)
            # This is the bring back focus to the browser from inspect elements
            auto.hotkey('alt')
        # To bring focus to the search bar.
        auto.hotkey('ctrl', 'l')

        # Generate a random question by choosing a random prefix and word
        auto.typewrite(random.choice(prefix) + " " + random.choice(words))
        auto.press("enter")  # Press the "enter" key
        time.sleep(search_delay)  # Pause for the specified search delay

    # To check whether the browser has lost focus or not.
    check_focus(required_window_id)
    if browser_close_var:
        close_browser()
    else:
        # To go to the Rewards site.
        auto.hotkey('ctrl', 'l')
        auto.typewrite("https://rewards.bing.com/")
        auto.press("enter")

        # Closes Inspect Elements
        auto.hotkey('ctrl', 'shift', 'i')

    # Re-enable Start Button
    start_button['state'] = 'enabled'


# Run the Tkinter main loop
root.mainloop()
