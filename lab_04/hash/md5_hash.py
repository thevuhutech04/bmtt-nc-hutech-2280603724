def left_rotate(value, shift):
    # Hàm quay trái 32-bit với số bit shift nhất định
    return ((value << shift) | (value >> (32 - shift))) & 0xFFFFFFFF

def md5(message):
    # Khởi tạo các giá trị ban đầu của a, b, c, d
    a = 0x67452301
    b = 0xEFCDAB89
    c = 0x98BADCFE
    d = 0x10325476

    original_length = len(message) * 8  # Đo chiều dài của message tính bằng bit
    message += b'\x80'  # Thêm bit 1 vào cuối
    while len(message) % 64 != 56:  # Padding các byte 0 để đảm bảo chiều dài phù hợp
        message += b'\x00'
    message += original_length.to_bytes(8, 'little')  # Thêm chiều dài thông điệp ban đầu

    # Hàm băm từng khối 512-bit
    for i in range(0, len(message), 64):
        block = message[i:i+64]
        words = [int.from_bytes(block[j:j+4], 'little') for j in range(0, 64, 4)]  # Chuyển block thành 16 từ 32-bit

        a0, b0, c0, d0 = a, b, c, d  # Lưu trữ giá trị ban đầu của a, b, c, d

        for j in range(64):
            if j < 16:
                f = (b & c) | ((~b) & d)
                g = j
            elif j < 32:
                f = (d & b) | ((~d) & c)
                g = (5 * j + 1) % 16
            elif j < 48:
                f = b ^ c ^ d
                g = (3 * j + 5) % 16
            else:
                f = c ^ (b | (~d))
                g = (7 * j) % 16

            # Tính toán vòng lặp MD5
            temp = d
            d = c
            c = b
            b = (b + left_rotate((a + f + 0x5A827999 + words[g]) & 0xFFFFFFFF, [7, 12, 17, 22][j % 4])) & 0xFFFFFFFF
            a = temp

        # Cập nhật giá trị của a, b, c, d
        a = (a + a0) & 0xFFFFFFFF
        b = (b + b0) & 0xFFFFFFFF
        c = (c + c0) & 0xFFFFFFFF
        d = (d + d0) & 0xFFFFFFFF

    # Kết quả là chuỗi MD5
    return '{:08x}{:08x}{:08x}{:08x}'.format(a, b, c, d)

# Nhập chuỗi cần băm
input_string = input("Nhập chuỗi cần băm: ")
md5_hash = md5(input_string.encode('utf-8'))

print("Mã băm md5 của chuỗi '{}' là : {}".format(input_string, md5_hash))
