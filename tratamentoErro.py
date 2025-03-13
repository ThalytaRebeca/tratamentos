while True:

    try: 
        n1 = int(input('Digite um número:  '))
        print()
        n2 = int(input('Digite outro número:  '))
        print()

        conta = n1 / n2

    except ZeroDivisionError:
        print('Não sei se você aprendeu isso na escola, mas não é possível dividir nada por zero 🙄🙄🙄')
        print()
    except ValueError:
        print('Apenas números inteiros permitidos! 😠😠😠😠')
        print()
    else:
        print(f'{n1} divido por {n2} é = {conta}')
        break

