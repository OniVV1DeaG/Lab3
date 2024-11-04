from turtledemo.penrose import start

from password import Password

class PasswordTable:

    def __init__(self, passwords : list) -> None:
        self.password_array = passwords

    def add_password(self, password : Password):
        self.password_array.append(password)

    def rem_password(self, passtext : str) -> bool:
        for i in self.password_array:
            if i.passtext == passtext:
                self.password_array.remove(i)
                return True
        return False

    def find_password(self, name : str) -> bool:
        for i in self.password_array:
            if i.login == name:
                return True
        return False

    def change_password(self, new_password : str, index : int) -> bool:
        if index < 0 or index >= len(self.password_array):
            return False
        self.password_array[index].passtext = new_password
        return True
