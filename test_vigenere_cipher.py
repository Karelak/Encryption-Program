
import unittest
from encryptionclasses import VigenereCipher

class TestVigenereCipher(unittest.TestCase):

    def test_encrypt(self):
        # Test encryption with a given key.
        plaintext = "ATTACKATDAWN"
        key = "LEMON"
        cipher = VigenereCipher(key, plaintext)
        encrypted = cipher.encrypt()
        self.assertEqual(encrypted, "LXFOPVEFRNHR")

    def test_decrypt(self):
        # Test decryption with a given key.
        ciphertext = "LXFOPVEFRNHR"
        key = "LEMON"
        cipher = VigenereCipher(key, ciphertext)
        decrypted = cipher.decrypt()
        self.assertEqual(decrypted, "ATTACKATDAWN")

    def test_non_alpha_characters(self):
        # Test that non-alphabetic characters are preserved.
        plaintext = "Hello, World!"
        key = "KEY"
        cipher = VigenereCipher(key, plaintext)
        encrypted = cipher.encrypt()
        cipher = VigenereCipher(key, encrypted)
        decrypted = cipher.decrypt()
        self.assertEqual(decrypted, plaintext)

if __name__ == '__main__':
    unittest.main()