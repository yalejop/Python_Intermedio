def run():
    my_list = [1, 'Hello', True, 4.5]
    my_dict = {'firstname': 'Facundo', 'lastname': 'Garcia'}

    super_list= [
        {'firstname': 'Facundo', 'lastname': 'Garcia'},
        {'firstname': 'Diana', 'lastname': 'Cataño'},
        {'firstname': 'Jorge', 'lastname': 'Villa'},
        {'firstname': 'Dario', 'lastname': 'Quintero'},
        {'firstname': 'Alexis', 'lastname': 'Pérez'},
    ]

    super_dict = {
        'natural_nums': [1, 2, 3, 4, 5],
        'integer_nums': [-1, -2, 0, 1, 2],
        'floating_nums': [1.1, 4.5, 6.43],
    }

    for key, value in super_dict.items():
        print(key, '-', value)

    for values in super_list:
        for key, value in values.items():
            print(key, '-', value) 



if __name__ == '__main__':
    run()