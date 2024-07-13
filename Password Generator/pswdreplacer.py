class PasswordSecurer:
    SECURE = (('per','%'),('s','$'),('and','&'),('er','^'),('o','0'),('a','@'),('i','1'))
    
    def __init__(self, password):
        self.password = password

    def secure_password(self):
        for a, b in self.SECURE:
            self.password = self.password.replace(a, b)
        return self.password

if __name__ == "__main__":
    pswd = input("Enter your password: ")
    password_securer = PasswordSecurer(pswd)
    secured_pswd = password_securer.secure_password()
    print(f"Your secure password is: {secured_pswd}")
