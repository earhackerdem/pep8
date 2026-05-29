# name = "Ana"

# text = f"Hola {name}"


# print(text)

# year = 2020
# text_format = "Hola {}".format(name)

# print(text_format)

# text_suma = f"Hola, {name} tu edad es: {2026 - year} años"

# print(text_suma)

# text_func = f"Hola {name.upper()}"
# print(text_func)

# edad = 20

# text_if = f"Hola {name}, eres {'mayor' if edad>= 18 else 'menor'} de edad"

# print(text_if)

bank_balance = 1200000000
text = f"Tu saldo en la cuenta bancaria es {bank_balance:,}:"
print(text)

stock_price = 1.405
text = f"El valor del stock es: {stock_price:.1f}"
print(text)

stock_price = 1.405
text = f"El valor del stock es: {stock_price:.2f}"
print(text)


user_id = 10000
text = f"Su ID es: {user_id:03d}"
print(text)

product = "Laptop"
price = 1000

text = f'Producto: {product:<15} | Precio {price:>10}'
print(f"{text}\n{text}")

from datetime import datetime

date = datetime(2024,12,5,10)

text = f"La fecha completa es {date: %A %d %Y}"

print(text)
