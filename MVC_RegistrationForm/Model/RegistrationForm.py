class RegistrationForm:
    def __init__(self, email, login, password):
        self.email = email
        self.login = login
        self.password = password

    def __str__(self):
        return f"'Email': '{self.email}', 'Login': '{self.login}', 'Password': '{self.password}'"