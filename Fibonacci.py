# def fibo(num):
#   ultimo = 1
#  penultimo = 0
# print(f'{penultimo} -> {ultimo}', end=' -> ')
# for c in range(num):
#   penultimo, ultimo = ultimo, penultimo + ultimo
#  print(ultimo, end=' -> ')

# print('Fim')


# fibo(40)

def fibonacci(quantidade, sequencia=(0, 1)):
    if len(sequencia) == quantidade:
        return sequencia
    return fibonacci(quantidade, sequencia + (sum(sequencia[-2:]),))


if __name__ == '__main__':
    for fib in fibonacci(20):
        print(fib, end=' -> ')
    print('fim')
