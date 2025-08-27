# Cryptographic-Protocol-Shapes-Analyzer-Meet-in-the-middle-Project
Analyzing the cryptographic weaknesses of 2DES and explaining why it doesn't work. Written in Python.

Implemented the Simplified Data Encryption Standard (S-DES), a Feistel cipher based off DES with a block size of 8-bits and a key size of 10-bits.

Meet in the Middle attack to determine the 20-bit key bundle (k1, k2) used in the Double S-DES encryption used in ECB mode to produce the following known plaintext/ciphertext pairs:


Plaintext/Ciphertext = 0x42/0x0f, 0x72/0x85, 0x75/0x3b, 0x74/0x2e, 0x65/0xed
Time the execution of your Meet in the Middle attack.


After finding the key with the Meet in the Middle attack, implement a simple brute force search for the key that searches from 0 to the key and time the execution of the brute force search.


After finding the key, use the key with the IV = 0xa6 to decrypt the following text that was encrypted using DS-DES in Cipher Block Chaining mode with the key you found. The encrypted text is ASCII so convert the output to ASCII characters to read the message.


Ciphertext in hexidecimal = 0xaa7a211c558bc0cedb51887f5e98de4d315b8b78cb39cb598c6b54cd6b54d5ef25a464c24e55dde1e4b3c477723c406d37fc6e0599e9d24d907849cd391267b6e3fe25f516accfbe297b4540078563fc25d0dbefc6e04fee3818d60aeec460798ad78d
