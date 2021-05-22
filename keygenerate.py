from cryptography.fernet import Fernet
print("your key is below")
key=Fernet.generate_key()
output = str(key, 'utf-8')
print(output)
