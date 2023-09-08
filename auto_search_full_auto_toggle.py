# For mobile rewards, run the code again, and before it starts searching,
# press Ctrl+Shift+I (to open inspect element), and then press Ctrl+Shift+M (to toggle the device mode)


# Import the necessary libraries
import pyautogui as auto  # Import the pyautogui library for automating GUI interactions
import time  # Import the time library for adding delays
import random  # Import the random library for generating random choices
import os  # Import the os library for interacting with the operating system

# Delay Variables
# If your pc is slow, or browser takes too much time then change these variables accordingly.
browser_open_delay = 2
inspect_element_delay = 1
search_delay = 1

# Define the path to the Microsoft Edge
# Put the path in a file called path.txt in the same directory.
# path_file = open('path.txt', 'r')
# browser_path = path_file.read()

path = "C:\\Program Files (x86)\\Microsoft\\Edge\\Application\\msedge.exe"

# Open Microsoft Edge Canary using the specified shortcut
os.startfile(path)

# Pause the script execution for 2 seconds to allow the browser to open
time.sleep(browser_open_delay)

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
         "Dimensionality Reduction", "Backpropagation", "Overfitting",
         "Underfitting", "Cross-Validation", "Natural Language Generation",
         "Supervised Learning", "Unsupervised Learning", "Neural Network Architecture",
         "Bias-Variance Tradeoff", "Feature Engineering", "Convolutional Neural Network",
         "Recurrent Neural Network", "Random Forest", "Gradient Descent"
]

# Opens Inspect Elements
auto.hotkey('ctrl', 'shift', 'i')
time.sleep(inspect_element_delay)

# Loop to automate a series of actions
for i in range(0, 6):
    if i == 3:
        # We are opening and closing inspect element so that the inspect element tab will get focus.
        auto.hotkey('ctrl', 'shift', 'i')
        time.sleep(inspect_element_delay)
        auto.hotkey('ctrl', 'shift', 'i')
        time.sleep(inspect_element_delay)
        # Toggles device mode
        auto.hotkey('ctrl', 'shift', 'M')
        time.sleep(inspect_element_delay)
    # Click at the search bar. If it isn't then update the x and y.
    auto.click(962, 51, clicks=1, button='left')

    # Generate a random question by choosing a random prefix and word
    auto.typewrite(random.choice(prefix) + " " + random.choice(words))
    auto.press("enter")  # Press the "enter" key
    time.sleep(search_delay)  # Pause for 1 second

# To go to the Rewards site.
auto.click(962, 51, clicks=1, button='left')
auto.typewrite("https://rewards.bing.com/")
auto.press("enter")

# Closes Inspect Elements
auto.hotkey('ctrl', 'shift', 'i')
#########################


# You don't have to run this part.
# I've included it here just in case you want to obtain the mouse position,
# allowing you to adjust the click coordinates if needed.
# While running the code below, please ensure that the code above is commented out.



# import pyautogui
# for i in range(0,10):
#     time.sleep(1)
#     # Get the current mouse pointer location as a tuple
#     pos = pyautogui.position()
#
#     # Unpack the X and Y coordinates from the tuple
#     x, y = pos
#
#     # Print the coordinates
#     print(f"Mouse pointer location - X: {x}, Y: {y}")

