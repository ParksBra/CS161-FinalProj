"""Drive crypto program."""

import sys
import crypto
import digest


def main():
    """Initialize program."""
    while True:
        option = str.lower(input("Would you like to encrypt or decrypt? (e/d): "))
        if option == "e" or option == "d":
            break
        continue
    if option == "e":
        return encrypt()
    elif option == "d":
        return decrypt()
    else:
        print("Fatal Error.")
        sys.exit()


def encrypt():
    """Create encrypted file."""
    select_file = str(input("Please name a txt file to encrypt: "))
    if select_file.lower()[len(select_file) - 4:len(select_file)] == ".txt":
        try:
            with open(select_file, "r") as input_file:
                input_str = input_file.read()
                encoded_str = digest.encode(input_str)
                cipher, key = crypto.encrypt(encoded_str)
                input_file.close()
        except FileNotFoundError:
            print("Error: File not found.")
            return encrypt()
        with open("encrypted.txt", "w") as output_file:
            output_file.write(str(cipher))
            output_file.close()
        with open("key.txt", "w") as key_file:
            key_file.write(str(key))
            key_file.close()
        print(f"Encryption of '{select_file}' completed successfully.\n\
Please check 'encrypted.txt'.")
    else:
        print("Error: Not .txt file.")
        return encrypt()


def decrypt():
    """Create decrypted file."""
    try:
        with open("encrypted.txt", "r") as encrypted_file:
            cipher = encrypted_file.read()
            encrypted_file.close()
    except FileNotFoundError:
        print("Error: 'encrypted.txt' not found.")
        return main()
    try:
        with open("key.txt", "r") as key_file:
            priv_key = key_file.read()
            key_file.close()
    except FileNotFoundError:
        print("Error: 'key.txt' not found.")
        return main()
    temp_key = ""
    key = []
    for i in priv_key:
        if i != ",":
            temp_key += i
        else:
            key.append(temp_key)
            temp_key = ""
    decrypted = crypto.decrypt(int(cipher), int(key[0]), int(key[1]))
    print(decrypted)
    plaintext = digest.decode(decrypted)
    print(plaintext)
    with open("decrypted.txt", "w") as output_file:
        output_file.write(str(plaintext))
        output_file.close()
    print("Decryption of 'encrypted.txt' completed successfully.\n\
Please check 'decrypted.txt'.")


if __name__ == "__main__":
    main()
