import os
import pyaes

# open and read encrypted file
encrypted_file_name = 'test.txt.ransomwaretroll'
file = open(encrypted_file_name, 'rb')
file_data = file.read()
file.close()

# decrypt key
key = b'testeransomwares'
aes = pyaes.AESModeOfOperationCTR(key)
decrypted_data = aes.decrypt(file_data)

# delete encrypted file
os.remove(encrypted_file_name)

# write decrypted file
new_file = 'test.txt'
new_file = open(new_file, 'wb')
new_file.write(decrypted_data)
new_file.close()
