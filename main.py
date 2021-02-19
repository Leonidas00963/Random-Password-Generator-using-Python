import random

chars = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789"

while 1:
    password_len = int(input(" length of your Password : "))
    password_count = int(1)
    password = ""
    for x in range(0, password_count):
        password = " "
        for x in range(0, password_len):
            password_char = random.choice(chars)
            password = password + password_char
        print("here is your password :", password)