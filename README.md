# Secure Hashing and Encryption

## Overview

This Python command-line application demonstrates SHA-256 hashing, Caesar cipher encryption and decryption, and RSA digital signatures.

## Features

- Generate a SHA-256 hash from a text string
- Generate a SHA-256 hash from a file
- Encrypt text using a Caesar cipher
- Decrypt Caesar-cipher text
- Generate an RSA private/public key pair
- Sign a file with the private key
- Verify a file signature with the public key

## Requirements

- Python 3.8 or newer
- The Python `cryptography` package

## Installation

Download or clone this repository and open a terminal in the project folder.

Install the required package:

```text
pip install -r requirements.txt
```

## Running the Application

Start the program with:

```text
python main.py
```

The following menu will appear:

```text
1. Generate a SHA-256 hash for text
2. Generate a SHA-256 hash for a file
3. Encrypt text with a Caesar cipher
4. Decrypt text with a Caesar cipher
5. Generate an RSA key pair
6. Sign a file
7. Verify a file signature
0. Exit
```

## SHA-256 Hashing

SHA-256 is a one-way cryptographic hash function. It converts text or file data into a fixed-length, 64-character hexadecimal value. Identical input produces the same hash, but even a small change to the input produces a different hash.

Example:

```text
Input: hello
SHA-256:
2cf24dba5fb0a30e26e83b2ac5b9e29e1b161e5c1fa7425e73043362938b9824
```

Use menu option 1 to hash text and option 2 to hash `sample.txt`.

## Caesar Cipher

The Caesar cipher replaces each letter with another letter a chosen number of positions away in the alphabet. Encryption shifts letters forward. Decryption shifts them backward by the same amount.

Example using a shift of 3:

```text
Original:  Hello World!
Encrypted: Khoor Zruog!
Decrypted: Hello World!
```

Spaces, punctuation, and letter capitalization are preserved.

## Digital Signatures

The application uses RSA public-key cryptography with SHA-256 and PSS padding.

- The private key signs the file.
- The public key verifies the signature.
- Verification succeeds when the file is unchanged.
- Verification fails if the file or signature has been modified.

To demonstrate the process:

1. Choose option 5 to generate the RSA key pair.
2. Choose option 6 and enter `sample.txt`.
3. The program creates `sample.txt.sig`.
4. Choose option 7.
5. Enter `sample.txt` as the original file.
6. Enter `sample.txt.sig` as the signature.
7. The program should report that verification succeeded.
8. Change the contents of `sample.txt` and verify it again to demonstrate a failed verification.

## Project Files
# Secure Hashing and Encryption

## Overview

This Python command-line application demonstrates SHA-256 hashing, Caesar cipher encryption and decryption, and RSA digital signatures.

## Features

- Generate a SHA-256 hash from a text string
- Generate a SHA-256 hash from a file
- Encrypt text using a Caesar cipher
- Decrypt Caesar-cipher text
- Generate an RSA private/public key pair
- Sign a file with the private key
- Verify a file signature with the public key

## Requirements

- Python 3.8 or newer
- The Python `cryptography` package

## Installation

Download or clone this repository and open a terminal in the project folder.

Install the required package:

```text
pip install -r requirements.txt
```

## Running the Application

Start the program with:

```text
python main.py
```

The following menu will appear:

```text
1. Generate a SHA-256 hash for text
2. Generate a SHA-256 hash for a file
3. Encrypt text with a Caesar cipher
4. Decrypt text with a Caesar cipher
5. Generate an RSA key pair
6. Sign a file
7. Verify a file signature
0. Exit
```

## SHA-256 Hashing

SHA-256 is a one-way cryptographic hash function. It converts text or file data into a fixed-length, 64-character hexadecimal value. Identical input produces the same hash, but even a small change to the input produces a different hash.

Example:

```text
Input: hello
SHA-256:
2cf24dba5fb0a30e26e83b2ac5b9e29e1b161e5c1fa7425e73043362938b9824
```

Use menu option 1 to hash text and option 2 to hash `sample.txt`.

## Caesar Cipher

The Caesar cipher replaces each letter with another letter a chosen number of positions away in the alphabet. Encryption shifts letters forward. Decryption shifts them backward by the same amount.

Example using a shift of 3:

```text
Original:  Hello World!
Encrypted: Khoor Zruog!
Decrypted: Hello World!
```

Spaces, punctuation, and letter capitalization are preserved.

## Digital Signatures

The application uses RSA public-key cryptography with SHA-256 and PSS padding.

- The private key signs the file.
- The public key verifies the signature.
- Verification succeeds when the file is unchanged.
- Verification fails if the file or signature has been modified.

To demonstrate the process:

1. Choose option 5 to generate the RSA key pair.
2. Choose option 6 and enter `sample.txt`.
3. The program creates `sample.txt.sig`.
4. Choose option 7.
5. Enter `sample.txt` as the original file.
6. Enter `sample.txt.sig` as the signature.
7. The program should report that verification succeeded.
8. Change the contents of `sample.txt` and verify it again to demonstrate a failed verification.

## Project Files

```text
main.py           Main application
requirements.txt  Required Python package
sample.txt        Example file for hashing and signing
README.md         Project documentation
.gitignore        Prevents generated and private files from being uploaded
```

## Security Note

The generated private and public keys are stored in the `keys` directory. That directory is excluded from GitHub by `.gitignore`. The private key should never be published or shared.

This project is for educational demonstration purposes.
```text
main.py           Main application
requirements.txt  Required Python package
sample.txt        Example file for hashing and signing
README.md         Project documentation
.gitignore        Prevents generated and private files from being uploaded
```

## Security Note

The generated private and public keys are stored in the `keys` directory. That directory is excluded from GitHub by `.gitignore`. The private key should never be published or shared.

This project is for educational demonstration purposes.
