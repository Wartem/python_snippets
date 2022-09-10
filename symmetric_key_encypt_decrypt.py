
from cryptography.fernet import Fernet

'''
Symmetric encryption.
Encrypt/decrypt with the same key.
'''

def encrypt(message, key):
    fernet = Fernet(key)
    
    return fernet.encrypt(message.encode())


def decrypt(encoded, key):
    fernet = Fernet(key)
    
    return fernet.decrypt(encoded).decode()


if __name__ == "__main__":
    with open ("example_text.txt", "r") as myfile:
        message = myfile.read()
        
        key = Fernet.generate_key()
        
        print("Message:", "\n"*2, message, "\n"*2)
        
        encrypted = encrypt(message, key)
        print("Encrypted:", "\n"*2, encrypted, "\n"*2)
        
        decrypted = decrypt(encrypted, key)
        print("Decrypted:", "\n"*2, decrypted)
