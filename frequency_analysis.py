import matplotlib.pyplot as plt
from collections import Counter

def frequency_analysis(text):
    # Count the frequency of each character in the text
    counter = Counter(text)
    
    # Separate the characters and their frequencies
    characters = list(counter.keys())
    frequencies = list(counter.values())
    
    # Plot the frequency analysis
    plt.figure(figsize=(10, 6))
    plt.bar(characters, frequencies, color='blue')
    plt.xlabel('Characters')
    plt.ylabel('Frequency')
    plt.title('Frequency Analysis')
    plt.show()