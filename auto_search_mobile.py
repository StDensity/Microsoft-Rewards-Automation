# For doing this you should open a new tab in mobile mode and have to perform one initial search by yourself.
# Then run this program, and you will get 2 seconds to switch to the browser.
# From there own it will do the searches on its own.

# MOBILE MODE SPECIFICATION
# Dimensions: Samsung Galaxy S20 Ultra  412 X 915


# Import the necessary libraries
import pyautogui as auto  # Import the pyautogui library for automating GUI interactions
import time  # Import the time library for adding delays
import random  # Import the random library for generating random choices

# Pause the script execution for 2 seconds
time.sleep(2)

# Define a list of prefixes to be used in generating questions
prefix = ["What is", "Define", "Explain", "Meaning of"]

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

# Loop to automate a series of actions
for i in range(0, 25):
    # Clicks at the search bar. Change the x, y if it isn't clicking the search bar.
    auto.click(1046, 170, clicks=1, button='left')
    time.sleep(0.1)  # Pause for 0.1 seconds
    # Click at the "X" button on the search bar. To clear the previous search.
    auto.click(1084, 170, clicks=1, button='left')
    time.sleep(0.1)  # Pause for 0.1 seconds

    # Generate a random question by choosing a random prefix and word
    auto.typewrite(random.choice(prefix) + random.choice(words))
    auto.press("enter")  # Press the "enter" key
    time.sleep(0.5)  # Pause for 0.5 seconds

#########################


# You don't have to run this part.
# I've included it here just in case you want to obtain the mouse position,
# allowing you to adjust the click coordinates if needed.

# import pyautogui
# import time
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
