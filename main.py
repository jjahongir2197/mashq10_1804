class User:
    def __init__(self, username, password):
        self.username = username
        self.password = password

    def login(self, username, password):
        if self.username == username and self.password == password:
            print("Login successful")
        else:
            print("Login failed")


def main():
    user = User("admin", "1234")

    user.login("admin", "1234")
    user.login("admin", "0000")


main()
