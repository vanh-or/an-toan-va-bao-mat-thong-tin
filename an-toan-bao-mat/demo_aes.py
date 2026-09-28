from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.primitives import padding
import os

def demo_aes():
    # 1. Khởi tạo khóa AES 256-bit và IV (Initialization Vector) 128-bit ngẫu nhiên
    key = os.urandom(32)  # 256 bits
    iv = os.urandom(16)   # 128 bits

    # Thông điệp ban đầu
    plaintext = "Chao mung ban den voi bai tap An toan va bao mat thong tin TNUT!".encode('utf-8')
    print("1. Plaintext ban dau:", plaintext.decode('utf-8'))

    # 2. Xử lý Padding cho dữ liệu (đạt chuẩn khối 128-bit)
    padder = padding.PKCS7(128).padder()
    padded_data = padder.update(plaintext) + padder.finalize()

    # 3. Mã hóa bằng AES-CBC
    cipher = Cipher(algorithms.AES(key), modes.CBC(iv))
    encryptor = cipher.encryptor()
    ciphertext = encryptor.update(padded_data) + encryptor.finalize()
    print("2. Ciphertext (da ma hoa - HEX):", ciphertext.hex())

    # 4. Giải mã
    decryptor = cipher.decryptor()
    decrypted_padded_data = decryptor.update(ciphertext) + decryptor.finalize()

    # Unpad dữ liệu
    unpadder = padding.PKCS7(128).unpadder()
    decrypted_data = unpadder.update(decrypted_padded_data) + unpadder.finalize()
    print("3. Plaintext sau khi giaima:", decrypted_data.decode('utf-8'))

if __name__ == "__main__":
    demo_aes()