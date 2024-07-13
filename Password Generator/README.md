# PasswordSecurer Class

## Overview
The `PasswordSecurer` class is designed to convert a user-provided password into a more secure format by replacing certain characters and substrings according to a predefined mapping.

## Class Definition

```python
class PasswordSecurer:
    SECURE = (('per','%'),('s','$'),('and','&'),('er','^'),('o','0'),('a','@'),('i','1'))
    
    def __init__(self, password):
        self.password = password

    def secure_password(self):
        for a, b in self.SECURE:
            self.password = self.password.replace(a, b)
        return self.password
