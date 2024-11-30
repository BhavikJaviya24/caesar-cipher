
# Caesar Cipher 🔒

This repository contains a simple Python implementation of the Caesar Cipher, a classic encryption technique. Encode or decode messages with a user-specified shift and secure your text-based secrets!

---

## Table of Contents

- [Features](#features)  
- [How It Works](#how-it-works)  
- [Installation](#installation)  
- [Usage](#usage)  
- [Technologies Used](#technologies-used)  
- [Future Improvements](#future-improvements)  
- [Contributing](#contributing)  

---

## Features  

- Encode messages by shifting each letter forward in the alphabet.  
- Decode messages by reversing the shift.  
- Handles non-alphabetic characters without modification.  
- Automatically adjusts shifts larger than 26 to wrap around the alphabet.  
- Interactive command-line interface for ease of use.  

---

## How It Works  

The Caesar Cipher works by shifting each letter of the input text by a fixed number of places in the alphabet. For example:
- Encoding `"abc"` with a shift of `2` produces `"cde"`.  
- Decoding `"cde"` with the same shift retrieves the original text, `"abc"`.  

Non-alphabetic characters (e.g., spaces, punctuation) are preserved as-is.  

---

## Installation  

1. Clone the repository:  
   ```bash
   git clone https://github.com/BhavikJaviya24/caesar-cipher.git
   cd caesar-cipher
   ```
2. Ensure you have Python 3 installed.  

---

## Usage  

1. Run the script:  
   ```bash
   python main.py
   ```
2. Follow the prompts:  
   - Enter "encode" to encrypt a message or "decode" to decrypt one.  
   - Provide the text and the shift value.  
   - View the result directly in the terminal!  
3. Choose to continue or exit after each operation.  

---

## Technologies Used  

- **Python 3.x**: Core programming language.  

---

## Future Improvements  

- Add support for uppercase letters without converting them to lowercase.  
- Build a graphical user interface (GUI) for easier use.  
- Include the ability to encrypt/decrypt files.  

---

## Contributing  

Contributions are welcome! Here's how you can help:  
- Report bugs or suggest new features via issues.  
- Fork the repository and submit a pull request with enhancements.  

---
