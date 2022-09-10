import rsa

'''
Symmetric encryption.
Encrypt/decrypt with the same key.
'''

def encrypt(message, key):
    return rsa.encrypt(message.encode(), publicKey)


def decrypt(encoded, key):
    return rsa.decrypt(encoded, privateKey).decode()


if __name__ == "__main__":
    with open ("example_text.txt", "r") as myfile:
        message = myfile.read()[:100]
        
        publicKey, privateKey = rsa.newkeys(1024)
        
        print("Message:", "\n"*2, message, "\n"*2)
        
        encrypted = encrypt(message, publicKey)
        print("Encrypted:", "\n"*2, encrypted, "\n"*2)
        
        decrypted = decrypt(encrypted, privateKey)
        print("Decrypted:", "\n"*2, decrypted)