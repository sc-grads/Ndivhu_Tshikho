
import unittest
from password_checker import validate_password, validate_password_with_error_messages

class TestValidatePassword(unittest.TestCase):
    def test_password_length(self):
        assert validate_password("short") == False
        assert validate_password("longpassword") == False

    def test_password_uppercase(self):
        assert validate_password("lowercase4!") == False
        assert validate_password("UPPERCASE4!") == False

    def test_password_lowercase(self):
        assert validate_password("lowercase") == False
        assert validate_password("UPPERCASE") == False 

    def test_password_digit(self):
        assert validate_password("password") == False
        assert validate_password("PASSWORD") == False

    def test_password_special_character(self):
        assert validate_password("password!") == False
        assert validate_password("password@") == False

class TestValidatePasswordWithErrorMessages(unittest.TestCase):
    def test_password_length(self):
        with self.assertRaises(ValueError):
            validate_password_with_error_messages("short")
        with self.assertRaises(ValueError):
            validate_password_with_error_messages("longpassword")   

    def test_password_uppercase(self):
        with self.assertRaises(ValueError):
            validate_password_with_error_messages("lowercase4!")
        with self.assertRaises(ValueError):
            validate_password_with_error_messages("UPPERCASE4!")   

    def test_password_lowercase(self):
        with self.assertRaises(ValueError):
            validate_password_with_error_messages("lowercase")
        with self.assertRaises(ValueError):
            validate_password_with_error_messages("UPPERCASE")   

    def test_password_digit(self):
        with self.assertRaises(ValueError):
            validate_password_with_error_messages("password")
        with self.assertRaises(ValueError):
            validate_password_with_error_messages("PASSWORD")   

    def test_password_special_character(self):
        with self.assertRaises(ValueError):
            validate_password_with_error_messages("password!")
        with self.assertRaises(ValueError):
            validate_password_with_error_messages("password@")  


if __name__ == '__main__':
    unittest.main()


