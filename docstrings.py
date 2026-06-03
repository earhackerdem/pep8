"""
Explicacion de docstrings

En esta clase puedo explicar como funcionan los docstrings en python

"""

def ejemplo_sin_docstring():
    return 'Hola Mundo'

def ejemplo_con_docstring():
    """
    DESCRIPTION
    ARGS
    RETURNS
    EXCEPTIONS
    EXAMPLES
    Returns:
        str: Un saludo en español
    """
    return 'Hola, mundo'

print(ejemplo_con_docstring.__doc__)
help(ejemplo_sin_docstring.__doc__)