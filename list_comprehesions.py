def run():

    square = [ i**2 for i in range(1, 101) if i % 3 != 0]
    # square = []
    # for i in range(1, 101):
    #     if i % 3 != 0:
    #      square.append(i**2)

    print(square)

    multiple_numbers = [ i for i in range(1, 10001) if i % 4 ==0 and i % 6 == 0 and i % 9 == 0]

    print(multiple_numbers)



if __name__ == '__main__':
    run()