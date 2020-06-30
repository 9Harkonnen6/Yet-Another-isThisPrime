while True:
    try:
        liczba = int(input('Wprowadź liczbę: '))
        
        if liczba > 0:
            for i in range(2, liczba):
                if (liczba % i) == 0:
                    print(liczba, 'NIE jest liczbą pierwszą')
                    break
            else:
                print(liczba, 'JEST PIERWSZĄ!')
        else:
            print('BŁĄD, LICZBA UJEMNA')
    except ValueError:
        print('Oops! To nie jest liczba')
