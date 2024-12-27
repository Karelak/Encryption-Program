# Encryption Program (OOP and Tkinter)

## Overview

This project is an encryption program built using Object-Oriented Programming (OOP) principles and the Tkinter library for the graphical user interface (GUI). The program allows users to encrypt and decrypt messages using various classical encryption algorithms.

## Features

- **User-friendly GUI** with real-time input validation
- **Multiple Encryption Algorithms**:
  - Caesar Cipher: Simple substitution cipher that shifts letters by a specified amount
  - Vernam Cipher: A stream cipher that uses a key of the same length as the plaintext
  - Vigenère Cipher: A polyalphabetic substitution cipher using a keyword
- **Real-time Validation**: Input fields are validated as you type with visual feedback
- **Frequency Analysis**: Analyze character frequency differences between input and output
- **Error Handling**: Clear error messages and input validation prevent invalid operations

## Requirements

- Python 3.x
- Tkinter (usually included with Python)
- Matplotlib (for frequency analysis)

## Installation

1. **Clone the repository:**

   ```sh
   git clone https://github.com/yourusername/encryption-program.git
   cd encryption-program
   ```

2. **Install required packages:**
   ```sh
   pip install -r requirements.txt
   ```

## Usage

1. **Start the program:**

   ```sh
   python main.py
   ```

2. **Using the Interface:**

   - Select an encryption algorithm (Caesar, Vernam, or Vigenère)
   - Choose between Encrypt or Decrypt operation
   - Enter your text in the plaintext field
   - Provide the required key or shift value:
     - Caesar: Enter a numerical shift value
     - Vernam: Enter a key of the same length as the input text
     - Vigenère: Enter any length key
   - Click "Submit" to perform the operation
   - Use "Frequency Analysis" to visualize character frequency changes
   - Access "Encryption Info" for algorithm descriptions

3. **Input Requirements:**
   - Caesar Cipher: Requires a numerical shift value
   - Vernam Cipher: Key must match plaintext length exactly
   - Vigenère Cipher: Requires any non-empty key

## Error Handling

The program includes comprehensive error handling:

- Invalid inputs are highlighted in red
- Error messages appear below the relevant input fields
- The Submit button is disabled until all inputs are valid

## Development

Built using:

- Python's OOP features for encapsulation and modularity
- Tkinter for the GUI implementation
- Matplotlib for frequency analysis visualization

## Contributing

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## License

This project is licensed under the Apache License 2.0 - see the `LICENSE` file for details.

## Contact

For any questions or suggestions, please contact [your email address].
