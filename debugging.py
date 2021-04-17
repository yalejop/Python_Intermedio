def divisor(num):
    divisor = []
    for i in range(1, num +1):
        if num % i == 0:
            divisor.append(i)
    return divisor


def run():
    num = int(input('Ingrese un número: '))
    print(divisor(num))
    print('Terminó mi programa')


if __name__ == '__main__':
    run()