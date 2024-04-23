#python
def caesar_encrypt(text, shift):
    encrypted_text = ""
    
    for char in text:
        if char.isalpha():
            if char.islower():
                encrypted_text += chr((ord(char) - ord('a') + shift) % 26 + ord('a'))
            else:
                encrypted_text += chr((ord(char) - ord('A') + shift) % 26 + ord('A'))
        else:
            encrypted_text += char
    
    return encrypted_text

def caesar_decrypt(text, shift):
    decrypted_text = ""
    
    for char in text:
        if char.isalpha():
            if char.islower():
                decrypted_text += chr((ord(char) - ord('a') - shift) % 26 + ord('a'))
            else:
                decrypted_text += chr((ord(char) - ord('A') - shift) % 26 + ord('A'))
        else:
            decrypted_text += char
    
    return decrypted_text

user_input = input("Enter a message to encrypt: ")
shift = int(input("Enter a shift value: "))

encrypted_message = caesar_encrypt(user_input, shift)
print("Encrypted message:", encrypted_message)

decrypted_message = caesar_decrypt(encrypted_message, shift)
print("Decrypted message:", decrypted_message)
