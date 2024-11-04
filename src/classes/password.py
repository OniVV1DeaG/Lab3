from datetime import datetime

class Password:
    def __init__(self, passtext : str, address : str, login : str, date : datetime) -> None:
        self.passtext = passtext
        self.address = address
        self.login = login
        self.date = date

    def __str__(self) -> str:
        return (f'Текст пароля: {self.passtext},'
                f'Адрес сайта: {self.address},'
                f'Логин пользователя: {self.login},'
                f'Дата записи пароля: {self.date}')