"""Secure Hashing and Encryption Assignment.

Features:
1. SHA-256 hashing for text
2. SHA-256 hashing for files
3. Caesar cipher encryption
4. Caesar cipher decryption
5. RSA digital signature creation and verification
"""

import hashlib
from pathlib import Path

try:
    from cryptography.exceptions import InvalidSignature
    from cryptography.hazmat.primitives import hashes, serialization
    from cryptography.hazmat.primitives.asymmetric import padding, rsa
except ImportError:
    print("Missing required package.")
    print("Install it with: pip install cryptography")
    raise SystemExit(1)


BASE_DIR = Path(__file__).resolve().parent
KEY_DIRECTORY = BASE_DIR / "keys"
PRIVATE_KEY_PATH = KEY_DIRECTORY / "private_key.pem"
PUBLIC_KEY_PATH = KEY_DIRECTORY / "public_key.pem"


def hash_text(text):
    """Return the SHA-256 hash of a text string."""
    return hashlib.sha256(text.encode("utf-8")).hexdigest()


def hash_file(file_path):
    """Return the SHA-256 hash of a file."""
    sha256 = hashlib.sha256()

    with file_path.open("rb") as file:
        while chunk := file.read(65_536):
            sha256.update(chunk)

    return sha256.hexdigest()


def caesar_cipher(text, shift):
    """Shift each letter while preserving case and punctuation."""
    result = []
    shift %= 26

    for character in text:
        if "A" <= character <= "Z":
            shifted = (ord(character) - ord("A") + shift) % 26
            result.append(chr(shifted + ord("A")))
        elif "a" <= character <= "z":
            shifted = (ord(character) - ord("a") + shift) % 26
            result.append(chr(shifted + ord("a")))
        else:
            result.append(character)

    return "".join(result)


def encrypt_text(text, shift):
    """Encrypt text using a Caesar cipher."""
    return caesar_cipher(text, shift)


def decrypt_text(text, shift):
    """Decrypt text using a Caesar cipher."""
    return caesar_cipher(text, -shift)


def generate_key_pair():
    """Generate an RSA private/public key pair."""
    if PRIVATE_KEY_PATH.exists() and PUBLIC_KEY_PATH.exists():
        print("\nA key pair already exists.")
        return

    KEY_DIRECTORY.mkdir(exist_ok=True)

    private_key = rsa.generate_private_key(
        public_exponent=65_537,
        key_size=2_048,
    )

    private_key_bytes = private_key.private_bytes(
        encoding=serialization.Encoding.PEM,
        format=serialization.PrivateFormat.PKCS8,
        encryption_algorithm=serialization.NoEncryption(),
    )

    public_key_bytes = private_key.public_key().public_bytes(
        encoding=serialization.Encoding.PEM,
        format=serialization.PublicFormat.SubjectPublicKeyInfo,
    )

    PRIVATE_KEY_PATH.write_bytes(private_key_bytes)
    PUBLIC_KEY_PATH.write_bytes(public_key_bytes)

    print("\nRSA key pair generated successfully.")
    print(f"Private key: {PRIVATE_KEY_PATH}")
    print(f"Public key:  {PUBLIC_KEY_PATH}")
    print("Important: Never upload the private key to GitHub.")


def sign_file(file_path):
    """Sign a file using the RSA private key."""
    generate_key_pair()

    private_key = serialization.load_pem_private_key(
        PRIVATE_KEY_PATH.read_bytes(),
        password=None,
    )

    file_data = file_path.read_bytes()

    signature = private_key.sign(
        file_data,
        padding.PSS(
            mgf=padding.MGF1(hashes.SHA256()),
            salt_length=padding.PSS.MAX_LENGTH,
        ),
        hashes.SHA256(),
    )

    signature_path = file_path.with_name(file_path.name + ".sig")
    signature_path.write_bytes(signature)

    print("\nFile signed successfully.")
    print(f"Original file: {file_path}")
    print(f"Signature file: {signature_path}")


def verify_signature(file_path, signature_path):
    """Verify a file using its signature and the RSA public key."""
    if not PUBLIC_KEY_PATH.exists():
        print("\nNo public key was found. Generate a key pair first.")
        return

    public_key = serialization.load_pem_public_key(
        PUBLIC_KEY_PATH.read_bytes()
    )

    file_data = file_path.read_bytes()
    signature = signature_path.read_bytes()

    try:
        public_key.verify(
            signature,
            file_data,
            padding.PSS(
                mgf=padding.MGF1(hashes.SHA256()),
                salt_length=padding.PSS.MAX_LENGTH,
            ),
            hashes.SHA256(),
        )
        print("\nVerification successful: the file has not been changed.")
    except InvalidSignature:
        print("\nVerification failed: the file or signature was changed.")


def request_file(prompt):
    """Ask for a file and make sure it exists."""
    entered_path = input(prompt).strip().strip('"')
    file_path = Path(entered_path).expanduser()

    if not file_path.is_absolute():
        file_path = BASE_DIR / file_path

    if not file_path.is_file():
        print(f"\nFile not found: {file_path}")
        return None

    return file_path


def request_shift():
    """Ask the user for a valid Caesar cipher shift."""
    while True:
        try:
            return int(input("Enter the shift number: "))
        except ValueError:
            print("Please enter a whole number.")


def display_menu():
    print("\nSecure Hashing and Encryption")
    print("--------------------------------")
    print("1. Generate a SHA-256 hash for text")
    print("2. Generate a SHA-256 hash for a file")
    print("3. Encrypt text with a Caesar cipher")
    print("4. Decrypt text with a Caesar cipher")
    print("5. Generate an RSA key pair")
    print("6. Sign a file")
    print("7. Verify a file signature")
    print("0. Exit")


def main():
    while True:
        display_menu()
        choice = input("\nChoose an option: ").strip()

        try:
            if choice == "1":
                text = input("Enter text to hash: ")
                print(f"\nOriginal text: {text}")
                print(f"SHA-256 hash: {hash_text(text)}")

            elif choice == "2":
                file_path = request_file("Enter the file path: ")
                if file_path:
                    print(f"\nFile: {file_path}")
                    print(f"SHA-256 hash: {hash_file(file_path)}")

            elif choice == "3":
                text = input("Enter text to encrypt: ")
                shift = request_shift()
                encrypted = encrypt_text(text, shift)

                print(f"\nOriginal text:  {text}")
                print(f"Shift:          {shift}")
                print(f"Encrypted text: {encrypted}")

            elif choice == "4":
                text = input("Enter text to decrypt: ")
                shift = request_shift()
                decrypted = decrypt_text(text, shift)

                print(f"\nEncrypted text: {text}")
                print(f"Shift:          {shift}")
                print(f"Decrypted text: {decrypted}")

            elif choice == "5":
                generate_key_pair()

            elif choice == "6":
                file_path = request_file("Enter the file to sign: ")
                if file_path:
                    sign_file(file_path)

            elif choice == "7":
                file_path = request_file("Enter the original file: ")
                if file_path:
                    signature_path = request_file(
                        "Enter the signature file: "
                    )
                    if signature_path:
                        verify_signature(file_path, signature_path)

            elif choice == "0":
                print("\nGoodbye!")
                break

            else:
                print("\nPlease choose an option from 0 through 7.")

        except OSError as error:
            print(f"\nFile operation failed: {error}")
        except ValueError as error:
            print(f"\nInvalid key or signature file: {error}")


if __name__ == "__main__":
    main()
