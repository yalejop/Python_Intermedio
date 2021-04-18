def divisor(num):
    divisor = []
    for i in range(1, num +1):
        if num % i == 0:
            divisor.append(i)
    return divisor


def run():
    num = input('Ingrese un número: ')
    assert num.isnumeric() and int(num) > 0, 'Debes Ingresar un Número Positivo'
    print(divisor(int(num)))
    print('Terminó mi programa')



if __name__ == '__main__':
    run()