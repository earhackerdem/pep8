# main.py Todo el código en un archivo
"""
Sistema de análisis de noticias con APIS múltiples
"""

# PEP 8: Configuracion centralizada - constantes en MAYÚSCULAS con guiones bajos
API_TIME_OUT = 30

MAX_TRIES = 3

DEFAULT_LANGUAGE = "es"  # PEP8 Comillas dobles para strings





# PEP 8 Utilidades comunes del proyecto - funciones snake_case
def clean_text(text):
    """
    Limpia y normaliza una cadena de texto.

    Elimina los espacios en blanco sobrantes al principio y al final de la
    cadena y convierte todos los caracteres a minúsculas. Si el texto de
    entrada está vacío o es None, devuelve una cadena vacía.

    Parameters
    ----------
    text : str or None
        El texto original que se desea limpiar y normalizar.

    Returns
    -------
    str
        El texto procesado en minúsculas y sin espacios en los extremos.

    Raises
    ------
    TypeError
        Si el argumento proporcionado no es una cadena de texto (str) o None.

    Examples
    --------
    >>> clean_text("  Hola Mundo  ")
    'hola mundo'
    >>> clean_text("")
    ''
    >>> clean_text(None)
    ''
    """
    # PEP8 4 espacios para indentacion, no tabs
    if not text:
        return ""
    
    if not isinstance(text, str):
        raise TypeError("El argumento 'text' debe ser una cadena de texto (str) o None.")
        
    return text.strip().lower()


# PEP8 Dobles lineas en blanco entre funciones para separar lógica
def validate_api_key(api_key):
    """Valida que la API KEY tenga formato correcto"""
    return len(api_key) > 10 and api_key.isanum()


def process_article_data(raw_data):
    """Procesa datos crudos de articulo"""
    pass


API_KEY = '7506b5608f2a47759e319524956f9055'


from news_analyzer.exceptions import APIKeyError
from news_analyzer.api_client import fetch_news
from news_analyzer.utils import get_sources

response_data = None

try:
    response_data = fetch_news('newsapi',api_key=API_KEY,query="Python")
except APIKeyError as e:
    print(f"{e}")
if response_data:
    
    source_set = get_sources(response_data['articles'])
    for index,source in enumerate(source_set,start=1):
        print(f'{index}:{source}')
    #print(source_set)
