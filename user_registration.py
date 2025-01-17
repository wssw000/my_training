def check_password(password):
    lower_set = 'abcdefghijklmnopqrstuvwxyz'
    upper_set = lower_set.upper()
    have_lower = False
    have_upper = False
    check_len = False

    if len(password) >=8:
        check_len = True
    else:
        print('слишком короткий пароль')
    for i in lower_set:
        if i in password:
            have_lower = True
        else:
            continue

    for i in upper_set:
        if i in password:
            have_upper = True
        else:
            continue

    if have_lower == True and have_upper == True and check_len == True:
        return True
    else:
        return False


class Database:
    def __init__(self):
        self.data = {}

    def add_user(self, username, password):
        self.data[username] = password


class User:
    """
    Класс пользователя содержащий атрибуты: логин, пароль

    """

    def __init__(self, username, password, password_confirm):
        self.username = username
        if password_confirm == password:
            self.password = password

if __name__ == '__main__':
    db = Database()
    while True:
        choise = int(input('Welcome! Select an action: \n1 - Log in \n2 - Sign up\n: '))
        if choise == 1:
            login = input('enter your login: ')
            password = input('enter your password: ')
            if login in db.data:
                if password == db.data[login]:
                    print(f'Welcome, {login}!!!')
                    exit()
                else:
                    print('invalid password')
            else:
                print('this user has not been found')

        if choise == 2:
            user = User(input('enter your username: '), password:=input('enter your passord: '),
                        password2:=input('confirm password: '))
            if password != password2:
                print('password dont match')
                continue
            if check_password(password) == False: #chek_password получает пароль, и возвращает True если пароль достаточно сложный
                print('incorrect password')
                continue
            db.add_user(user.username, user.password)
        print(db.data)