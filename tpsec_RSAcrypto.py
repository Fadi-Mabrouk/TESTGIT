import random

# Function to check if a number is prime
def is_prime(num):
    if num <= 1:
        return False
    if num <= 3:
        return True
    if num % 2 == 0 or num % 3 == 0:
        return False
    i = 5
    while ((i*i) <= num):
        if num % i == 0 or num % (i + 2) == 0:
            return False
        i += 6
    return True

# Function to find the greatest common divisor (GCD) of two numbers
def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

# Function to generate a random prime number
def generate_prime(bits):
    while True:
        num = random.getrandbits(bits)
        if is_prime(num):
            return num

# Function to calculate the modular inverse
def mod_inverse(a, m):
    m0, x0, x1 = m, 0, 1
    while a > 1:
        q = a // m
        m, a = a % m, m
        x0, x1 = x1 - q * x0, x0
    return x1 + m0 if x1 < 0 else x1

# Key generation
def generate_keypair(bits):
    p = generate_prime(bits)
    q = generate_prime(bits)
    n = p * q
    phi = (p - 1) * (q - 1)

    e = 65537  # A common choice for the public exponent

    # Ensure e and phi(n) are coprime
    while gcd(e, phi) != 1:
        e = random.randrange(2, phi)

    d = mod_inverse(e, phi)

    public_key = (n, e)
    private_key = (n, d)
    return public_key, private_key

# Encryption
def encrypt(public_key, plaintext):
    n, e = public_key
    encrypted = [pow(ord(char), e, n) for char in plaintext]
    return encrypted

# Decryption
def decrypt(private_key, encrypted):
    n, d = private_key
    decrypted = [chr(pow(char, d, n)) for char in encrypted]
    return ''.join(decrypted)

# Test the RSA encryption and decryption
message = "This is a secret message."
bits = 1024
public_key, private_key = generate_keypair(bits)

encrypted_message = encrypt(public_key, message)
decrypted_message = decrypt(private_key, encrypted_message)

print("Original message:", message)
print("Decrypted message:", encrypted_message)


'''def generate_keypair(p, q):
    n = p * q
    phi = (p - 1) * (q - 1)
    
    e = 65537  # Commonly used value
    d = pow(e, -1, phi)

    return (e, n), (d, n)

def encrypt_message(message, e, n):
    m = int.from_bytes(message.encode(), byteorder='big')
    c = pow(m, e, n)
    return c

def decrypt_message(c, d, n):
    m = pow(c, d, n)
    decrypted_message = m.to_bytes((m.bit_length() + 7) // 8, byteorder='big').decode()
    return decrypted_message

# Example key generation
p = 5  # Replace with a large prime number
q = 11  # Replace with another large prime number
public_key, private_key = generate_keypair(p, q)

# Example usage
message_to_encrypt = "Hello, RSA encryption!"
encrypted_message = encrypt_message(message_to_encrypt, *public_key)
print(f"Encrypted message: {encrypted_message}")

decrypted_message = decrypt_message(encrypted_message, *private_key)
print(f"Decrypted message: {decrypted_message}")'''
