def main():
    print('Welcome to email slicer' +'\n')

    email_input = input('Enter your email address: ')
    (username, domain) = email_input.split('@')
    (domain, extension) = domain.split('.')


    print(f'username: {username}')
    print(f'domain: {domain}')

main()