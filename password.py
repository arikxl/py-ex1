import random
import string

characters = list(string.ascii_letters + string.digits +
                  "!@#$%^&*()*+,-./:;<=>>")


def generate_password():
    password_length = int(input('How long do you want your password? '))

    random.shuffle(characters)
    password = []

    for x in range(password_length):
        password.append(random.choice(characters))

    random.shuffle(password)
    password = ''.join(password)
    print(password)


generate_password()
