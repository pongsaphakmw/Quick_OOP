def greeting_without_parameter():
    print('Hello World!')


def greeting_with_parameter(name):
    print('Hello', name)


def greeting_with_return(name):
    return 'Hello ' + name

if __name__ == '__main__':
    print()
    print('This is outputs')
    print('calling greeting_without_parameter()')
    greeting_without_parameter()
    print('printing greeting_without_parameter()')
    print(greeting_without_parameter())
    print('calling greeting_with_parameter(\'John\')')
    greeting_with_parameter('John')
    print('calling greeting_with_return(\'Bob\')')
    greeting_with_return('Bob')
    print('printing greeting_with_return(\'Bob\')')
    print(greeting_with_return('Bob'))
    print()


