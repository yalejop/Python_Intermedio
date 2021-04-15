from math import sqrt

def run():

    # dict_list = {}

    # for i in range(1, 101):
    #     if i % 3 != 0:
    #         dict_list[i] = i**3
    
    dict_list = {i: i**3 for i in range(1, 101) if i % 3 != 0}

    sqrt_numbers = {i: sqrt(i) for i in range(1, 1001)}

    print(dict_list)

    print(sqrt_numbers)
        


if __name__ == '__main__':
    run()