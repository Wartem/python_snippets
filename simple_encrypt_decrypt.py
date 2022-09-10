'''

This is a version of the Caesar cipher,
https://en.wikipedia.org/wiki/Caesar_cipher

A very simple way of encrypting and decrypting a text.

The encoding is reversed and the text
can be restored.

The text is encrypted and the encrypted text
is concated with the lengths of all the words.
At the end, the number of words is concated. 

'''

encode_word = lambda x: chr(ord(x)+99)
decode_word = lambda x: chr(ord(x)-99)

def simple_encrypt(message):
    
    encoded = message.split()
    
    encoded = [list(map(encode_word, word)) 
               for _, word in enumerate(encoded)]

    long_string = [''.join(word) for word in encoded]
    
    number_of_splits = len(encoded)
    len_of_splits = [len(word) for word in encoded]
    
    encode_lengths = list([chr(x + 199) 
                           for x in len_of_splits])
    encode_num_of_splits = chr(number_of_splits + 199)

    encoded = [*long_string, *encode_lengths, encode_num_of_splits]
    encoded = ''.join(encoded)
    
    return encoded.encode()

def simple_decrypt(encoded: str):
    
    encoded = encoded.decode()
    number_of_words = ord(encoded[-1]) - 199
    len_of_words = [ord(encoded[i]) - 199 
                    for i in range(len(encoded) - number_of_words - 1, len(encoded) - 1)]
    
    coded_message = encoded[:len(encoded) - number_of_words - 1]

    words = []
    start = 0
    end = 0
    
    for len_ in len_of_words:
        end += len_
        words.append(coded_message[start:end])
        start += len_
        
    encoded = [list(map(decode_word, word)) for word_index, word in enumerate(words)]
    encoded = [''.join(word) for word in encoded]
    message = ' '.join(encoded)
    
    return message
    
def main():
    
    with open ("example_text.txt", "r") as myfile:
        message = myfile.read()
        
        #message = "Jag måste ringa min konstantinopelopanska basfiolsfodralsmakargesäll"
        
        print("Message:", "\n"*2, message, "\n"*2)
        
        encrypted = simple_encrypt(message)
        print("encrypted", "\n"*2, encrypted, "\n"*2)
        
        decrypted = simple_decrypt(encrypted)
        print("decrypted", "\n"*2, decrypted)

if __name__ == '__main__':
    main()