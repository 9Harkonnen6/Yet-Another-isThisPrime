while True:
    try:
        liczba = int(input('Give me a number: '))
        
        if liczba > 0:
            for i in range(2, liczba):
                if (liczba % i) == 0:
                    print(liczba, 'That aint prime number!')
                    break
            else:
                print(liczba, 'YEAH, IT IS A PRIME!')
        else:
            print('ERROR, input <0')
    except ValueError:
        print('Oops! That aint number at all!')
