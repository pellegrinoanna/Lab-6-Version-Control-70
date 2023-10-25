
def encoder(password):
    new_pass = ''
    for item in password:
        item = int(item) + 3
        new_pass += str(item)
    return new_pass

if __name__ == "__main__" :
    password = input()
    print(encoder(password))
