def decimal_to_roman(number):
    if not (1 <= number <= 3999):
        raise ValueError("Número fuera de rango (1-3999)")

    val = [
        (1000, 'M'), (900, 'CM'),
        (500, 'D'), (400, 'CD'),
        (100, 'C'), (90, 'XC'),
        (50, 'L'), (40, 'XL'),
        (10, 'X'), (9, 'IX'),
        (5, 'V'), (4, 'IV'),
        (1, 'I')
    ]

    result = ""
    for (arabic, roman) in val:
        while number >= arabic:
            result += roman
            number -= arabic
    return result

def main():
    try:
        entrada = input("Ingresá un número del 1 al 3999: ")
        numero = int(entrada)
        romano = decimal_to_roman(numero)
        print(f"Número romano: {romano}")
    except ValueError as e:
        print(f"Error: {e}")
    except Exception:
        print("Entrada inválida. Debe ser un número entero.")


if __name__ == "__main__":
    main()