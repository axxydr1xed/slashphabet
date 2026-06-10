# Imports
from time import sleep as slp
from slashdata import SLASHPHABET, ALPHABET, DIGITS, SLASHGITS
print("Hello! This is a decoder for the cipher made by Qwuikky.")
slp(1)
# Funcs
def encode():
    text = input("Input the text you want to encode: ")
    encoded = ""
    for char in text:
        if char.lower() in ALPHABET or char.lower() in DIGITS:
            if char.lower() in ALPHABET:
                encoded += ALPHABET[char.lower()]
            elif char.lower() in DIGITS:
                encoded += DIGITS[char.lower()]
            else:
                pass
        else:
            encoded += char
    print("Encoded text: " + encoded)

def decode():
    text = input("Input the text you want to decode: ")
    decoded = ""
    i = 0
    while i < len(text):
        if text[i] == '[':
            # Find the closing bracket
            j = i + 1
            while j < len(text) and text[j] != ']':
                j += 1
            if j < len(text):  # Found closing bracket
                pattern = text[i:j+1]
                if pattern in SLASHPHABET or pattern in SLASHGITS:
                    if pattern in SLASHPHABET:
                        decoded += SLASHPHABET[pattern]
                    elif pattern in SLASHGITS:
                        decoded += SLASHGITS[pattern]
                else:
                    decoded += pattern
                i = j + 1
            else:
                decoded += text[i]
                i += 1
        elif text[i] == ' ':
            decoded += ' '
            i += 1
        else:
            decoded += text[i]
            i += 1
    print("Decoded text: " + decoded)

# Choice loop
print("""
   What to do?   
1. Encode
2. Decode
3. Exit
""")
while True:
    choice = input("Enter your choice: ")
    if choice not in ['1', '2', '3']:
        print("Invalid choice. Try again.")
        continue
    elif choice == '1':
        encode()
    elif choice == '2':
        decode()
    elif choice == '3':
        print("Goodbye!")
        break