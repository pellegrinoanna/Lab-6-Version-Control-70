
def encoder(password):
    new_pass = ''
    for item in password:
        item = int(item) + 3
        new_pass += str(item)
    return new_pass

def decoder(new_password):
    decoded = ''
    for item in new_password:
        item = int(item) - 3
        decoded += str(item)
    return decoded

if __name__ == "__main__" :
    menu = True
    while True:
        print('Menu')
        print('-------------')
        print('1. Encode')
        print('2. Decode')
        print('3. Quit')
        print('Please enter an option:')
        option = int(input())

        if option == 1:
            print('Please enter your password to encode:')
            password = input()
            new_password = encoder(password)
            print('Your password has been encoded and stored!')

        elif option == 2:
            decode_password = decoder(new_password)
            print(f'The encoded password is {new_password} and the original password is {decode_password}. ')

        elif option == 3:
            menu = False
