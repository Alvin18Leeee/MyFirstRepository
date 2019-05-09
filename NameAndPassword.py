while True:
    print('What is your name?')
    name = input()
    if name != 'Alvin':
        continue
    print('Hi, Alvin. What is the password?')
    while True:
        password = input()
        if password != '123456':
            print('Access Denied. Plz try again.')
            continue
        print('Access Granted.')
        break
    break
