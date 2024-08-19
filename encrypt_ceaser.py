# Define the list of alphabet characters
alphabet = [chr(i) for i in range(ord('a'), ord('z') + 1)]

def encrypt_decrypt(text, mode, key):
    text_encrypt_decrypt = ''

    if mode == 'd':
        key = -key

    for i in text:
        if i == ' ':
            text_encrypt_decrypt += ' '
        else:
            index = alphabet.index(i)
            new_index = (index + key) % 26
            text_encrypt_decrypt += alphabet[new_index]
    
    return text_encrypt_decrypt

print()
print('Caesar cipher program')
print()

print('Do you want to encrypt or decrypt?')
user_input = input('e/d: ').lower()
print()

if user_input == 'e':
    print('Encryption mode selected')
    key = int(input('Enter key: '))
    text = input('Enter the text: ')
    ciphertext = encrypt_decrypt(text, user_input, key)
    print(f'Ciphertext is: {ciphertext}')

elif user_input == 'd':
    print('Decryption mode selected')
    key = int(input('Enter key: '))
    text = input('Enter the text: ')
    plaintext = encrypt_decrypt(text, user_input, key)
    print(f'Plaintext is: {plaintext}')
