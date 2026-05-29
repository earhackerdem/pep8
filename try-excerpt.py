a = 0
b = 0
try:
    a = int(input("Digita un número"))
    b = int(input('Digita otro número'))
    resultado = a/b
    print(f"Resultado:{resultado}")
except ValueError:
    print('El valor que digito no es un numero valido')
except ZeroDivisionError:
    print('No se puede dividir por cero')
finally:
    print('Print desde finally')

print('Este es otro print')



