from cryptography.fernet import Fernet
from ProjectManagement import settings

encryption_key = settings.FIELD_ENCRYPTION_KEY
cipher_suite = Fernet(encryption_key)

def encryptOtp(otp):
    encrypted = cipher_suite.encrypt(otp.encode())
    return encrypted.decode()

def decryptOtp(encryptedOtp):
    decrypted = cipher_suite.decrypt(encryptedOtp.encode())
    return decrypted.decode()