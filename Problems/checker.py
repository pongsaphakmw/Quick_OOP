def check_result(data, result):
    with open(data, 'r') as f:
        with open(result, 'r') as f2:
            if f.read() == f2.read():
                print('Correct')
            else:
                print('Wrong')