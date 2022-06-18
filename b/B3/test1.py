user_database = {
    'user': 'password',
    'iseedeadpeople': 'greedisgood',
    'hesoyam': 'tgm'
}

def check_user(username, password):
    if username in user_database:
        if password in user_database.get(username):
            return True
        else:
            return False

username = input("Input name:")
password = input("Input password:")
print(check_user(username, password))
