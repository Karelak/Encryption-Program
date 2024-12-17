import matplotlib.pyplot as plt
from collections import Counter

def frequency_analysis(input_text: str, output_text: str):
    """Perform frequency analysis on the given input and output texts and display a bar graph of the positive frequency difference."""
    input_counter = Counter(input_text)
    output_counter = Counter(output_text)
    
    characters = list(set(input_counter.keys()).union(set(output_counter.keys())))
    input_frequencies = [input_counter[char] for char in characters]
    output_frequencies = [output_counter[char] for char in characters]
    frequency_difference = [max(0, output_frequencies[i] - input_frequencies[i]) for i in range(len(characters))]
    
    plt.figure(figsize=(10, 6))
    plt.bar(characters, frequency_difference, color='blue')
    plt.xlabel('Characters')
    plt.ylabel('Positive Frequency Difference')
    plt.title('Frequency Analysis (Positive Output - Input)')
    plt.show()