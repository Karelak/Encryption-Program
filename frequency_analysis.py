import matplotlib.pyplot as plt
from collections import Counter

def frequency_analysis(text: str):
    counter = Counter(text)
    characters = list(counter.keys())
    frequencies = list(counter.values())
    
    plt.figure(figsize=(10, 6))
    plt.bar(characters, frequencies, color='blue')
    plt.xlabel('Characters')
    plt.ylabel('Frequency')
    plt.title('Frequency Analysis')
    plt.show()