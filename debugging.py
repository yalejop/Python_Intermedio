def divisor(num):
    divisor = []
    for i in range(1, num +1):
        if num % i == 0:
            divisor.append(i)
    return divisor


def run():
    try:
        num = int(input('Ingrese un número: '))
        if num < 0 or num == 0:
            raise Exception('Solo Ingresa valores Positivos')
        print(divisor(num))
        print('Terminó mi programa')
    except ValueError:
        print('Debes ingresar una Número')
    except Exception:
        print('Debes ingresar un número positivo')

if __name__ == '__main__':
    run()