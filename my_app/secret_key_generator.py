import os
import binascii

for i in range(1, 6):
    print(binascii.hexlify(os.urandom(24)).decode('utf-8'))

# 选一个作为secret_key
