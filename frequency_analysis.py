import matplotlib.pyplot as plt
from collections import Counter

# Function to perform frequency analysis on the given text
def frequency_analysis(text):
    # Count the frequency of each character in the text
    counter = Counter(text)
    
    # Separate the characters and their frequencies
    characters = list(counter.keys())
    frequencies = list(counter.values())
    
    # Plot the frequency analysis
    plt.figure(figsize=(10, 6))  # Set the figure size
    plt.bar(characters, frequencies, color='blue')  # Create a bar chart
    plt.xlabel('Characters')  # Label for x-axis
    plt.ylabel('Frequency')  # Label for y-axis
    plt.title('Frequency Analysis')  # Title of the plot
    plt.show()  # Display the plot