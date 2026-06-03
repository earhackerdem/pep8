"""Typing con Python"""

variable = 42 
print(f"Variable {variable}, del tipo {type(variable)}")

variable = 'Texto de prueba'
print(f"Variable {variable}, del tipo {type(variable)}")

# variable: tipo = valor

otra_variable: int = 44
print(f"Variable {otra_variable}, del tipo {type(otra_variable)}")

otra_variable = 'Texto'

user_id: int | None = None

def suma_clara(a: int,b: int) -> int:
    return a +b

articles: list[dict] = [
    {
        "title":'Example'
    },
    {
        'title': 'Example 2'
    }
]

articles_dos: list[list][str] = [
    ['lista','lista'],
    ['lista','lista']
]

